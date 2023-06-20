from django import forms
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
class LogForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'maxlength' : "30", 'placeholder' : 'Enter Username'}),error_messages={'username' : {'required' : "Username can't be empty"}})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input', 'maxlength' : "30", 'placeholder' : 'Enter Password'}), error_messages={'password' : {'required' : "Password can't be empty" }})
class ForgotPswd(SetPasswordForm):
    new_password1 = forms.CharField(label="New password",widget=forms.TextInput(attrs={'class':'input', 'maxlength' : "30", }),error_messages={'username' : {'required' : "Username can't be empty"}})
    new_password2 = forms.CharField(label="New password confirmation",widget=forms.TextInput(attrs={'class':'input', 'maxlength' : "30", }),error_messages={'username' : {'required' : "Username can't be empty"}})

           
