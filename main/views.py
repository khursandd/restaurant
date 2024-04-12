from django.shortcuts import render
from django.views import View



class HomeView(View):
    def get(self, request):
        context = {
            'title': 'Home page',
        }
        return render(request, 'index.html', context)

