import uuid
from django.db import models
from users.models import User


class Board(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, related_name="boards", on_delete=models.CASCADE)
