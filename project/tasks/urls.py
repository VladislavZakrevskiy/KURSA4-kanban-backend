from django.urls import path
from .views import createTask, getTasksByColumn, updateTask, deleteTask

urlpatterns = [
    path("create", createTask, name="create task"),
    path("by-column/<uuid:columnId>", getTasksByColumn, name="get tasks by col"),
    path("update/<uuid:id>", updateTask, name="update task"),
    path("<uuid:id>", deleteTask, name="delete task"),
]
