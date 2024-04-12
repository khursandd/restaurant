from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate

from accounts import forms
from accounts import models


class LogInView(View):
    def get(self, request):
        form = forms.LogInForm()
        context = {
            'title': 'Log In',
            'form': form
        }
        return render(request, 'registration/login.html', context)

    def post(self, request):
        form = forms.LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user, backend=None)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
        context = {
            'title': 'Log In',
            'form': form,
        }
        return render(request, 'registration/login.html', context)


class SignInView(View):
    def get(self, request):
        form = forms.SignInForm()
        context = {
            'title': 'Sign In',
            'form': form,
        }
        return render(request, 'registration/signin.html', context)

    def post(self, request):
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                form.add_error('password2', 'Password do not match')
                return render(request, 'registration/signin.html', {'form': form, 'title': 'Sing In'})
            user = models.Customer.objects.create_user(username=username, password=password1)
            login(request, user)
            return redirect('home')
        return render(request, 'registration/signin.html', {'form': form, 'title': 'Sign In'})

