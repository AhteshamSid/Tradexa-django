from django.contrib import admin
from .models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'weight', 'price', 'created_at', 'updated_at']

# Register your models here.
