from rest_framework import serializers
from ..models import Task, Column


class CreateTask(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description"]

    def create(self, validated_data):
        column = Column.objects.get(id=self.context["columnId"])
        return Task.objects.create(column=column, **validated_data)
