from django import forms
from django.contrib.auth.models import User
from fourthapp.models import ProfileInfo


class UserInfo(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','password','email')

class ProfileInfoForm(forms.ModelForm):
    class Meta():
        model=ProfileInfo
        fields=('userlink','user_image')
