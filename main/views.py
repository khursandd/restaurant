from django.shortcuts import render
from django.views import View

from main import models


class HomeView(View):
    def get(self, request):
        context = {
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

