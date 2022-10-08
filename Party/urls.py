from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Party'

urlpatterns = [
    path('create-parties',views.parties,name='createparty'),
    path('parties-data',views.displayparties,name='displayparties'),
]