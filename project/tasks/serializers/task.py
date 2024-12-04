from rest_framework import serializers
from ..models import Task
from subtasks.serializers.subtask import SubtaskSerializer


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True)

    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "subtasks"]
