from django.db import models
import uuid


class Comments(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    content = models.CharField(max_length=255, unique=True)

    movie = models.OneToOneField('movies.Movies', on_delete = models.CASCADE)
    user = models.OneToOneField('users.User', on_delete = models.CASCADE)
    