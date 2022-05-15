from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from .models import UserInfo

class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')
class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=('git_url','profile_pic')
class LoginForm(forms.Form):
    username=forms.CharField(max_length=150,label='Your Name:')
    password=forms.CharField(widget=forms.PasswordInput())