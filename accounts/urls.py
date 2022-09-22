from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.login,name='LoginPage'),
    path('index/',views.home,name='Home'),
]