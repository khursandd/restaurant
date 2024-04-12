from django import forms

from accounts import models


class LogInForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")








