from django.db import models

# Create your models here.


class MovieModel(models.Model):
    name = models.CharField(max_length=250)
    year = models.IntegerField()
    desc = models.TextField()
    img = models.ImageField(upload_to="MovieImg")

    def __str__(self):
        return self.name
