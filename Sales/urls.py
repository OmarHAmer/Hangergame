from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Sales'

urlpatterns = [
    path('create-room',views.rooms,name='createroom'),
    path('room-data',views.displayrooms,name='displayrooms'),
]