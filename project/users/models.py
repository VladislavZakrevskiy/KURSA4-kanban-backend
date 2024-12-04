import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
