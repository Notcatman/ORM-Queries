from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=200, null=False)
    genre = models.CharField(max_length=200, null=False)
    duration_minutes = models.IntegerField(null=False, validators=[MaxValueValidator(999), MinValueValidator(1)], default=1)
    rating = models.FloatField(null=False, validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return f"{self.title}"
    
class Viewer(models.Model):
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=250, null=False)
    age = models.IntegerField(null=False, validators=[MaxValueValidator(90), MinValueValidator(6)])
    email = models.EmailField(null=True, blank=True)
    is_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.surname}'
    
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE, null=True, blank=True)
    score = models.IntegerField(null=False, validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return f'{self.viewer} rated movie "{self.movie}" - {self.score} stars'
    