from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    movie_logo = models.FileField()
    movie_desc=models.CharField(max_length=300)
    main_actor=models.CharField(max_length=300)
    director=models.CharField(max_length=300)
    length_movie=models.CharField(max_length=300)
    release_time=models.CharField(max_length=300)
    country=models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Myrating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

class MyList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watch = models.BooleanField(default=False)
