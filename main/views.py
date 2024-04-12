from django.shortcuts import render
from django.views import View

from accounts import models as acc_models
from main import models


class HomeView(View):
    def get(self, request):
        products = models.Product.objects.all()
        context = {
            'products': products,
            'title': 'Home page',
        }
        return render(request, 'index.html', context)


class ProductDetailView(View):
    def get(self, request, slug):
        product = models.Product.objects.get(slug=slug)
        context = {
            'title': product.title,
            'product': product,
        }
        return render(request, 'product_detail.html', context)


class AboutView(View):
    def get(self, request):
        context = {
            'title': 'About we',
        }
        return render(request, 'about.html', context)


class AboutRestaurantView(View):
    def get(self, request, username):
        restaurant = acc_models.Restaurant.objects.get(username=username)
        context = {
            'title': restaurant.username,
            'restaurant': restaurant,
        }
        return render(request, 'about_restaurant.html', context)