from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers.createTask import CreateTask
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers.task import TaskSerializer


@swagger_auto_schema()
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getTasksByColumn(request: Request, columnId: str):
    tasks = Task.objects.all().filter(column_id=columnId)
    return Response(
        TaskSerializer(tasks, many=True).data,
    )


@swagger_auto_schema()
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createTask(request: Request):
    serializer = CreateTask(
        data=request.data, context={"columnId": request.data["columnId"]}
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"error": "error"}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema()
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def updateTask(request: Request, id: str):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        print("ERROR Task Does not exist")

    serializer = TaskSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({"error": "error"}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema()
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteTask(request: Request, id: str):
    Task.objects.get(id=id).delete()
    return Response({"message": "success!"})
