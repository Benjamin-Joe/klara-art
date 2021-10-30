from django.contrib import admin
from .models import Products, Category


# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'image',
        'price',
    )


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category)
