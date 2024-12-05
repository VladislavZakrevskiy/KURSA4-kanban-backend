from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers.subtask import SubtaskSerializer
from rest_framework import status
from .models import Subtask


@swagger_auto_schema()
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createSubtask(request: Request):
    serializer = SubtaskSerializer(
        data=request.data, context={"taskId": request.data["taskId"]}
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"error": "error"}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema()
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getTask(request: Request, id: str):
    task = Subtask.objects.all().filter(task_id=id)
    return Response(SubtaskSerializer(task, many=True).data)


@swagger_auto_schema()
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def updateTask(request: Request, id: str):
    try:
        subtask = Subtask.objects.get(id=id)
    except Subtask.DoesNotExist:
        print("ERROR Does not subtask")
    serializer = SubtaskSerializer(subtask, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({"error": "error"}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema()
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleleSubtask(request: Request, id: str):
    Subtask.objects.get(id=id).delete()
    return Response({"message": "success!"})
