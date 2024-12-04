from django.db import models
import uuid
from columns.models import Column


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)
    column = models.ForeignKey(Column, related_name="tasks", on_delete=models.CASCADE)
