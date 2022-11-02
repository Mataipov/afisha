from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Film(models.Model):

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=250)
    rating = models.FloatField(default=0)
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='film_list', null=True)


    def __str__(self):
        return self.title