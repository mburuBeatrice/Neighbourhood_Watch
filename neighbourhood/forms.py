from django import forms
from .models import Neighbourhood,Business

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = [' neighbourhood_name',' neighbourhood_location','occupation_count'] 

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['business_name',' business_email_address']