from rest_framework import serializers
from ..models import Column
from boards.models import Board


class CreateColumn(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ["id", "title", "description"]

    def create(self, validated_data):
        print(validated_data)
        board = Board.objects.get(id=self.context["boardId"])
        return Column.objects.create(board=board, **validated_data)
