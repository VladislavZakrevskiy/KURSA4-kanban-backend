from rest_framework import serializers
from ..models import Board


class CreateBoard(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ["id", "title", "description"]

    def create(self, validated_data):
        user = self.context["request"].user
        return Board.objects.create(user=user, **validated_data)
