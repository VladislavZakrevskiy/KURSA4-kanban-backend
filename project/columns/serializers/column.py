from rest_framework import serializers
from ..models import Column
from tasks.serializers.task import TaskSerializer


class ColumnSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)  # Вложенный сериализатор для тасков

    class Meta:
        model = Column
        fields = ["id", "title", "description", "tasks"]
