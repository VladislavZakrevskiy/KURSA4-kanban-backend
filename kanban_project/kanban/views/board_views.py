from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models import Board
from ..serializers.db_serializers import BoardSerializer


@swagger_auto_schema(method="get", responses={200: BoardSerializer(many=True)})
@api_view(["GET"])
def get_boards(request):
    """Получить все доски."""
    boards = Board.objects.all()
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method="get", responses={200: BoardSerializer, 404: "Доска не найдена"}
)
@api_view(["GET"])
def get_board_by_id(request, board_id):
    """Получить доску по ID."""
    try:
        board = Board.objects.get(id=board_id)
        serializer = BoardSerializer(board)
        return Response(serializer.data)
    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method="post",
    request_body=BoardSerializer,
    responses={201: BoardSerializer, 400: "Ошибка в данных запроса"},
)
@api_view(["POST"])
def create_board(request):
    """Создать новую доску."""
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid():
        board = serializer.save()
        return Response(BoardSerializer(board).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="patch",
    request_body=BoardSerializer,
    responses={
        200: BoardSerializer,
        404: "Доска не найдена",
        400: "Ошибка в данных запроса",
    },
)
@api_view(["PATCH"])
def update_board(request, board_id):
    """Обновить существующую доску по ID."""
    try:
        board = Board.objects.get(id=board_id)
        serializer = BoardSerializer(board, data=request.data, partial=True)
        if serializer.is_valid():
            board = serializer.save()
            return Response(BoardSerializer(board).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method="delete", responses={204: "Доска удалена", 404: "Доска не найдена"}
)
@api_view(["DELETE"])
def delete_board(request, board_id):
    """Удалить доску по ID."""
    try:
        board = Board.objects.get(id=board_id)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "userId": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="ID пользователя, с которым делится доска",
            ),
        },
        required=["userId"],
    ),
    responses={200: "Board shared successfully", 400: "Ошибка в данных запроса"},
)
@api_view(["POST"])
def share_board(request, board_id):
    """Совместное использование доски с другим пользователем."""
    user_id = request.data.get("userId")
    # Логика для совместного использования доски с пользователем
    return Response({"message": "Board shared successfully"}, status=status.HTTP_200_OK)
