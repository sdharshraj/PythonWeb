from django.contrib import admin
from .models import Product
from .models import Offers

class ProductAdmin(admin.ModelAdmin) : 
    list_display = ('name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin) : 
    list_display = ('code', 'description')

admin.site.register(Product, ProductAdmin)
admin.site.register(Offers, OfferAdmin)