from django.urls import path
from .views import createSubtask, getTask, deleleSubtask, updateTask

urlpatterns = [
    path("create", createSubtask, name="create subtask"),
    path("by-task/<uuid:id>", getTask, name="get subtask by task"),
    path("update/<uuid:id>", updateTask, name="update subtasks"),
    path("<uuid:id>", deleleSubtask, name="delete subtask"),
]
