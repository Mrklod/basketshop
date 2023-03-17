from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('profile/',profile,name='profile'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('catalog/',catalog,name='catalog')
]