from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..serializers.auth_serializer import RegisterSerializer, LoginSerializer


@swagger_auto_schema(
    method="post",
    request_body=RegisterSerializer,
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "user": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "username": openapi.Schema(
                            type=openapi.TYPE_STRING,
                        ),
                        "email": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
                "access_token": openapi.Schema(type=openapi.TYPE_STRING),
                "refresh_token": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        400: "Invalid input data",
    },
)
@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    """Регистрация нового пользователя."""
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


@swagger_auto_schema(
    method="post",
    request_body=LoginSerializer,
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "user": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "username": openapi.Schema(type=openapi.TYPE_STRING),
                        "email": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
                "access_token": openapi.Schema(type=openapi.TYPE_STRING),
                "refresh_token": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        400: "Invalid input data",
        401: "Invalid credentials",
    },
)
@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    """Логин пользователя с получением токенов."""
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


@swagger_auto_schema(
    method="get",
    responses={
        200: openapi.Response(
            description="Profile data",
            examples={
                "application/json": {
                    "user": {"username": "example", "email": "example@example.com"},
                }
            },
        ),
        401: "Unauthorized",
    },
)
@api_view(["GET"])
def get_profile(request):
    """Получение данных профиля текущего пользователя."""
    user = request.user
    if user.is_authenticated:
        return Response(
            {"user": {"username": user.username, "email": user.email}},
            status=status.HTTP_200_OK,
        )
    return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
