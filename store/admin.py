from django.contrib import admin
from .models import Category, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'stock', 'category','is_available']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)