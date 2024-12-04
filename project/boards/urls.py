from django.urls import path
from .views import (
    createBoard,
    getBoardsWithAllDetails,
    getUserBoards,
    getBoardById,
    updateBoard,
    deleteBoard,
)

urlpatterns = [
    path("create", createBoard, name="create board"),
    path("details", getBoardsWithAllDetails, name="get boards with all details"),
    path("", getUserBoards, name="Get user boards"),
    path("delete/<uuid:id>", deleteBoard, name="delete board"),
    path("<uuid:id>", getBoardById, name="Get board by id"),
    path("update/<uuid:id>", updateBoard, name="update board"),
]
