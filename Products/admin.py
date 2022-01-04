from django.contrib import admin
from Products.models import Product

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):

    list_display = ['name','weight','price','created_at','updated_at']