from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models import Task, Column
from ..serializers.db_serializers import TaskSerializer


@swagger_auto_schema(method="get", responses={200: TaskSerializer(many=True)})
@api_view(["GET"])
def get_tasks_by_column(request, column_id):
    """Получение задач по ID колонки."""
    tasks = Task.objects.filter(column__id=column_id)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method="post",
    request_body=TaskSerializer,
    responses={
        201: TaskSerializer,
        400: "Ошибка в данных запроса",
    },
)
@api_view(["POST"])
def create_task(request):
    """Создание новой задачи."""
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="patch",
    request_body=TaskSerializer,
    responses={
        200: TaskSerializer,
        404: "Задача не найдена",
        400: "Ошибка в данных запроса",
    },
)
@api_view(["PATCH"])
def update_task(request, task_id):
    """Обновление задачи по ID."""
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="delete", responses={204: "Задача удалена", 404: "Задача не найдена"}
)
@api_view(["DELETE"])
def delete_task(request, task_id):
    """Удаление задачи по ID."""
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Task.DoesNotExist:
        return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method="patch",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "newColumnId": openapi.Schema(
                type=openapi.TYPE_STRING, description="ID новой колонки"
            ),
        },
        required=["newColumnId"],
    ),
    responses={200: TaskSerializer, 404: "Задача или колонка не найдена"},
)
@api_view(["PATCH"])
def move_task(request, task_id):
    """Перемещение задачи в другую колонку."""
    new_column_id = request.data.get("newColumnId")
    try:
        task = Task.objects.get(id=task_id)
        new_column = Column.objects.get(id=new_column_id)
        task.column = new_column
        task.save()
        return Response(TaskSerializer(task).data)
    except Task.DoesNotExist:
        return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    except Column.DoesNotExist:
        return Response(
            {"detail": "Column not found"}, status=status.HTTP_404_NOT_FOUND
        )
