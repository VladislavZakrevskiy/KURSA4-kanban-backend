from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)


class Board(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Column(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE)


class Task(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)


class Subtask(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
