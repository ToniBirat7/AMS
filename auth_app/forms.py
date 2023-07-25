from django import forms
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from Attendance.models import Person

class LogForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'maxlength' : "30", 'placeholder' : 'Enter Username'}),error_messages={'username' : {'required' : "Username can't be empty"}})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input', 'maxlength' : "30", 'placeholder' : 'Enter Password'}), error_messages={'password' : {'required' : "Password can't be empty" }})
class ForgotPswd(SetPasswordForm):
    new_password1 = forms.CharField(label="New password",widget=forms.TextInput(attrs={'class':'input', 'maxlength' : "30", }),error_messages={'username' : {'required' : "Username can't be empty"}})
    new_password2 = forms.CharField(label="New password confirmation",widget=forms.TextInput(attrs={'class':'input', 'maxlength' : "30", }),error_messages={'username' : {'required' : "Username can't be empty"}})


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'address', 
            'DOB', 
            'primary_number', 
            'secondary_number', 
            'sex', 
            'my_image', 
            'is_student',
        ]
        widgets = {
            'address': forms.TextInput(attrs={'class': 'custom-class'}),
            'DOB': forms.DateInput(attrs={'class': 'custom-class', 'type': 'date'}),
            'primary_number': forms.TextInput(attrs={'class': 'custom-class'}),
            'secondary_number': forms.TextInput(attrs={'class': 'custom-class'}),
            'sex': forms.Select(attrs={'class': 'custom-class'}),
            'my_image': forms.FileInput(attrs={'enctype': 'multipart/form-data'}),
            'is_student': forms.CheckboxInput(attrs={'class': 'custom-class'}),
        }
    
    

           
