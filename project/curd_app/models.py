from django.db import models


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    movieTitle = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    reviewContent = models.CharField(max_length=200)
    rating = models.IntegerField()
    reviewer_email_id = models.EmailField()
    genres = models.CharField(max_length=200)

