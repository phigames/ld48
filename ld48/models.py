import uuid
from typing import Optional

from django.db import models


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.TextField()
    average_rating = models.FloatField(default=0)
    n_ratings = models.PositiveIntegerField(default=0)
    username = models.CharField(max_length=30)
    image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def add_rating(self, rating: float, old_rating: Optional[float] = None):
        ratings_sum = self.average_rating * self.n_ratings
        ratings_sum += rating
        if old_rating is not None:
            ratings_sum -= old_rating
        else:
            self.n_ratings += 1
        self.average_rating = ratings_sum / self.n_ratings
        self.save()
