from django import forms
from django.contrib.auth.models import User

class LogForm(forms.ModelForm):
    
    class Meta:
       
        model = User
        fields = ['username','password']
        error_messages = {
            'username' : {'required' : "Username can't be empty" },
            'password' : {'required' : "Username can't be empty" }
            
        }
        widgets = {'password' : forms.PasswordInput(attrs={'class':'input', 'maxlength' : "30" , 'placeholder' : 'Enter Password'}), 
                   'username' : forms.TextInput(attrs={'class':'input', 'maxlength' : "30", 'placeholder' : 'Enter Username'})}
      
           
