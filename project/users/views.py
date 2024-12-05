from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers.login import LoginSerializer
from .serializers.register import RegisterSerializer


@api_view(["POST"])
@swagger_auto_schema(
    request_body=RegisterSerializer,
    responses={
        status.HTTP_201_CREATED: openapi.Response(
            description="User registered successfully",
            method="POST",
            examples={
                "application/json": {
                    "user": {"username": "user1", "email": "user1@example.com"},
                    "access_token": "access_token_string",
                    "refresh_token": "refresh_token_string",
                }
            },
        ),
        status.HTTP_400_BAD_REQUEST: "Invalid data provided",
    },
)
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "user": {"username": user.username, "email": user.email},
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            },
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@swagger_auto_schema(
    request_body=LoginSerializer,
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Login successful",
            examples={
                "application/json": {
                    "user": {"username": "user1", "email": "user1@example.com"},
                    "access_token": "access_token_string",
                    "refresh_token": "refresh_token_string",
                }
            },
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            description="Invalid credentials",
            examples={"application/json": {"detail": "Invalid credentials"}},
        ),
        status.HTTP_400_BAD_REQUEST: "Invalid data provided",
    },
)
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "user": {"username": user.username, "email": user.email},
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh),
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@swagger_auto_schema(
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="User profile retrieved successfully",
            examples={
                "application/json": {
                    "user": {"username": "user1", "email": "user1@example.com", "id": 1}
                }
            },
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            description="Unauthorized",
            examples={"application/json": {"error": "Unauthorized"}},
        ),
    }
)
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    if user.is_authenticated:
        return Response(
            {"user": {"username": user.username, "email": user.email, "id": user.id}},
            status=status.HTTP_200_OK,
        )
    return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
