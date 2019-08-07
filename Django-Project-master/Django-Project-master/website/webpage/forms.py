from django import forms
import os
from django.conf import settings
class rform(forms.Form):
    fname = forms.CharField(label="First Name",max_length=50)
    lname = forms.CharField(label="Last Name",max_length=50)
    uname = forms.CharField(label="Username",max_length=50)
    email = forms.EmailField(label="Email",max_length=50)
    upassword = forms.CharField(label="Password",widget=forms.PasswordInput,max_length=50)
    urepassword = forms.CharField(label="Confirm",max_length=50,widget=forms.PasswordInput)
class lform(forms.Form):
    uname = forms.CharField(label="Username",max_length=100)
    upassword = forms.CharField(label="Password",widget=forms.PasswordInput,max_length=50)
