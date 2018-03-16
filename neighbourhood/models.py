from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=30)
    neighbourhood_location = models.CharField(max_length=30)
    occupation_count = models.CharField(max_length=30)
    user = models.ForeignKey(User,default=1)

    def __str__(self):
        return self.neighbourhood_name

