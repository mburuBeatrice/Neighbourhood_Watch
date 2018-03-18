from django import forms
from .models import Neighbourhood,Business,Posts

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = [' neighbourhood_name',' neighbourhood_location','occupation_count'] 

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['business_name',' business_email_address']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['post']