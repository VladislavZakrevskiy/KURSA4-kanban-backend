from rest_framework import serializers
from ..models import Board


class UpdateBoard(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ["id", "title", "description"]

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.save()

        return instance
