from django import forms
class ImageForm(forms.Form):
    image = forms.ImageField(label="Upload Pic",widget=forms.FileInput(attrs={'class': 'image'}))

        
