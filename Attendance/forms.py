from django import forms
from .models import Person
class ImageForm(forms.Form):
    image = forms.ImageField(label="Choose Pic",label_suffix='',widget=forms.FileInput(attrs={'class': 'image'}))


        
