from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from .models import Column
from .serializers.createColumn import CreateColumn
from .serializers.column import ColumnSerializer
from .serializers.updateColumn import UpdateColumn


@swagger_auto_schema()
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createColumn(request: Request):
    print(request.data)
    serializer = CreateColumn(
        data=request.data, context={"boardId": request.data["boardId"]}
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema()
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getBoardColumn(request: Request, id: str):
    columns = Column.objects.all().filter(board_id=id)
    serializer = ColumnSerializer(columns, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema()
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def updateColumn(request: Request, id: str):
    try:
        column = Column.objects.get(id=id)
    except Column.DoesNotExist:
        return Response(
            {"detail": "Column not found"}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = UpdateColumn(column, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema()
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteBoardColumn(request: Request, id: str):
    Column.objects.get(id=id).delete()
    return Response({"message": "success!"}, status=status.HTTP_200_OK)
