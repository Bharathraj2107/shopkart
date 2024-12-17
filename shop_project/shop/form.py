from django.contrib.auth.forms import UserCreationForm
from.models import User
from django import forms
class CustomUserForm(UserCreationForm):#we inherit the usercreationform and we are going to override its class
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']#pswd1 is normal pswd and pswd2 is the confirm pswd