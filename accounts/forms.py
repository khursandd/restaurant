from django import forms

from accounts import models


class LogInForm(forms.Form):
    username = forms.CharField(max_length=64, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class SignInForm(forms.Form):
    username = forms.CharField(max_length=64, label='Username')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Password')









