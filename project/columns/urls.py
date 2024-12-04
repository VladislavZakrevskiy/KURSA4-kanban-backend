from django.urls import path
from .views import createColumn, getBoardColumn, deleteBoardColumn, updateColumn

urlpatterns = [
    path("create", createColumn, name="create column"),
    path("<uuid:id>", getBoardColumn, name="get columns by board id"),
    path("update/<uuid:id>", updateColumn, name="update columns"),
    path("delete/<uuid:id>", deleteBoardColumn, name="delete columns"),
]
