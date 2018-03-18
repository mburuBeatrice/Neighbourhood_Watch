from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=30)
    neighbourhood_location = models.CharField(max_length=30)
    occupation_count = models.CharField(max_length=30)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.neighbourhood_name

    
    def create_neighbourhood(self):
        return self.save()

    def delete_neighbourhood(self):
        return self.remove()

    def find_neighbourhood(neighbourhood_id):
        neighbourhood = Neighbourhood.objects.filter(neighbourhood_id = id)
        return neighbourhood
    @classmethod
    def update_neighbourhood(cls, id, neighbourhood_name):
        update_neighbourhood = Neighbourhood.objects.filter(id=id).update(neighbourhood_name = neighbourhood_name)
        return update_neighbourhood

    @classmethod
    def update_occupants(cls, id, occupation_count):
        update_occupants =  neighbourhood_update = Neighbourhood.objects.filter(id=id).update(occupation_count = occupation_count)
        return update_occupants()




# class User(models.Model):
#     name = models.CharField(max_length=30)
#     neighbourhood = models.ForeignKey(Neighbourhood)
#     email_address = models.EmailField()



# class Business(models.Model):
#     business_name = models.CharField(max_length=30)
#     user = models.ForeignKey(User)
#     neighbourhood = models.ForeignKey(Neighbourhood)
#     business_email_address = models.EmailField()