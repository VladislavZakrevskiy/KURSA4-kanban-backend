from rest_framework import serializers
from ..models import Board
from columns.serializers.column import ColumnSerializer


class BoardSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True)

    class Meta:
        model = Board
        fields = ["id", "title", "description", "columns"]
