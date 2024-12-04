import uuid
from django.db import models
from boards.models import Board


class Column(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    board = models.ForeignKey(Board, related_name="columns", on_delete=models.CASCADE)
