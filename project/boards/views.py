from .models import Board
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers.board import BoardSerializer
from .serializers.createBoard import CreateBoard
from .serializers.updateBoard import UpdateBoard

# POST create board with cols ✅
# GET Get boards with all details ✅
# GET Get boards of user ✅
# GET Get board with id ✅
# PATCH Update Board ✅
# DELETE delte Board


@swagger_auto_schema()
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createBoard(request: Request):
    serializer = CreateBoard(data=request.data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema()
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getBoardsWithAllDetails(request: Request):
    boards = Board.objects.prefetch_related("columns__tasks__subtasks").all()
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema()
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUserBoards(request: Request):
    boards = (
        Board.objects.prefetch_related("columns__tasks__subtasks")
        .all()
        .filter(user_id=request.user.id)
    )
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema()
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getBoardById(request: Request, id: str):
    board = Board.objects.prefetch_related("columns__tasks__subtasks").get(id=id)
    serializer = BoardSerializer(board)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema()
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def updateBoard(request: Request, id: str):
    try:
        board = Board.objects.get(id=id)
    except Board.DoesNotExist:
        return Response({"detail": "Board not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UpdateBoard(board, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema()
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteBoard(request: Request, id: str):
    board = Board.objects.get(id=id).delete()
    return Response({"message": "success!"}, status=status.HTTP_200_OK)
