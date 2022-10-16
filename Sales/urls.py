from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Sales'

urlpatterns = [
    path('create-room',views.rooms,name='createroom'),
    path('room-data',views.displayrooms,name='displayrooms'),
    path('create-price-list',views.createprice,name='createprice'),
    path('price-list-data',views.displaypricelist,name='displaypricelist'),
    path('create-order',views.createorder,name='createorder'),
    path('order-data',views.displayorder,name='displayorder'),
    path('create-customer',views.createpartyfromorder,name='createcustomerfromorder'),
    path('create-room-order',views.createroomfromorder,name='createroomfromorder'),
]