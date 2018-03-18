from django import forms
from .models import Neighbourhood,Business,Posts

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['user'] 

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','neighbourhood']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['post']