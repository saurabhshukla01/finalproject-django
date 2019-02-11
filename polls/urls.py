from django.urls import path
from .views import *

urlpatterns = [
    path('',register,name='register'),
    path('login/',loginuser,name='login'),
    path('logout/',logoutuser,name='logout')
]