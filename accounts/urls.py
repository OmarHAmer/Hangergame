from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.login,name='LoginPage'),
    path('Home/',views.home,name='Home'),
    path('<str:app>/<str:slug>',views.navpage,name='navpage'),
]