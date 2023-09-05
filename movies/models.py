from django.db import models
import uuid


class Movies(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    classification = models.IntegerField()
    url = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)
    background = models.CharField(max_length=255)
    sinopse = models.CharField(max_length=255)
    actors = models.CharField(max_length=255)
    directors = models.CharField(max_length=255)

    user = models.ForeignKey('users.User', on_delete = models.CASCADE, related_name = 'movies')