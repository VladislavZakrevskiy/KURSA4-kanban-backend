from rest_framework import serializers
from ..models import Subtask


class SubtaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subtask
        fields = ["id", "title", "description", "is_done"]
