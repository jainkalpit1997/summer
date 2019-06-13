from django import forms
from django.contrib.auth.models import User
class signup(forms.ModelForm):
    # username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput())
    # email=forms.CharField(widget=forms.EmailInput())
    class Meta:
        model=User
        fields=('username','email','password')
