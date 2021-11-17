from django.urls import path, include

from .views import login_page, logout_page,user,register

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('user/', user, name='user'),
    path('register/', register, name='register'),

]