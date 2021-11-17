from django.urls import path, include

from .views import order, delivery

urlpatterns = [
    path('order/', order, name='order'),
    path('delivery/', delivery, name='delivery'),

]