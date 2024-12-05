from rest_framework import serializers
from ..models import Subtask
from tasks.models import Task


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ["id", "title", "is_done"]

    def create(self, validated_data):
        task = Task.objects.get(id=self.context["taskId"])
        validated_data["is_done"] = False
        return Subtask.objects.create(task=task, **validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.is_done = validated_data.get("is_done", instance.is_done)
        instance.save()

        return instance
