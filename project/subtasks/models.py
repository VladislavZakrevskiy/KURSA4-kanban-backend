import uuid
from django.db import models
from tasks.models import Task


class Subtask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    task = models.ForeignKey(Task, related_name="subtasks", on_delete=models.CASCADE)
