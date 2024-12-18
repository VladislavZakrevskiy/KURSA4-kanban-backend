from rest_framework import serializers
from ..models import Task
from subtasks.serializers.subtask import SubtaskSerializer


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True)

    class Meta:
        model = Task
        fields = ["id", "title", "description", "subtasks"]

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.save()

        return instance
