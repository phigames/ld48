import uuid

from django.db import models


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.TextField()
    upvotes = models.IntegerField(default=0)
    username = models.CharField(max_length=30)
