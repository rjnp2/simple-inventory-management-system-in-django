from django.urls import path, include

from .views import product,product_delete

urlpatterns = [
    path('product/', product, name='product'),
    path('product/delete/<int:id>/', product_delete, name='product_delete'),
]