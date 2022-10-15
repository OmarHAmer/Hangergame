from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Inventory'

urlpatterns = [
    path('master-items',views.master_items,name='master_items'),
    path('items-data',views.displayitems,name='displayitems'),
    path('create-cat',views.creatcatfromitems,name='creatcatfromitems'),
]