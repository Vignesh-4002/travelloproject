from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('credentials/', views.credentials, name='credentials'),
    path('userlogin/', views.userlogin,name='userlogin'),
    path('userlogout/',views.userlogout,name='userlogout')

]
