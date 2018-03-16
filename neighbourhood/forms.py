from django import forms
from .models import Neighbourhood

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = [' neighbourhood_name',' neighbourhood_location','occupation_count']