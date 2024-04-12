from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate

from accounts import forms


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
