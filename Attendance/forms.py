from django import forms
from .models import Person
class ImageForm(forms.Form):
    image = forms.ImageField(label="Upload Pic",widget=forms.FileInput(attrs={'class': 'image'}))


        
