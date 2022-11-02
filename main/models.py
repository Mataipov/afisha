from django.db import models

# Create your models here.
class Film(models.Model):

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=250)
    rating = models.FloatField(default=0)
    duration = models.FloatField()


    def __str__(self):
        return self.title