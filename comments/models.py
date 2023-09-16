from django.db import models
import uuid


class Comments(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    content = models.CharField(max_length=255, unique=True)

    movie = models.ForeignKey('movies.Movies', on_delete = models.CASCADE, related_name='comments')
    user = models.ForeignKey('users.User', on_delete = models.CASCADE, related_name='comments')
    