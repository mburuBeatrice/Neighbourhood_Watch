from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=30)
    neighbourhood_location = models.CharField(max_length=30)
    occupation_count = models.CharField(max_length=30)
    user = models.ForeignKey('User')

    def __str__(self):
        return self.neighbourhood_name

class User(models.Model):
    name = models.CharField(max_length=30)
    neighbourhood = models.ForeignKey(Neighbourhood)
    email_address = models.EmailField()



class Business(models.Model):
    business_name = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    neighbourhood = models.ForeignKey(Neighbourhood)
    business_email_address = models.EmailField()