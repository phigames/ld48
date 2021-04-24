import uuid

from django.db import models


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.TextField()
    average_rating = models.FloatField(null=True)
    n_ratings = models.PositiveIntegerField(default=0)
    username = models.CharField(max_length=30)

    def add_rating(self, rating: float):
        ratings_sum = self.average_rating * self.n_ratings
        ratings_sum += rating
        self.n_ratings += 1
        self.average_rating = ratings_sum / self.n_ratings
        self.save()
