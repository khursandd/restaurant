from django.contrib import admin

from main import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']