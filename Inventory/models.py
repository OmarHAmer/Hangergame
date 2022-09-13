from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class RowColumn(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(User, on_delete=models.CASCADE, blank=False)
    Last_update_date = models.DateTimeField(auto_now=True)
    Last_update_by = models.IntegerField(User, on_delete=models.CASCADE, blank=False)

    class Meta:
        abstract = True
        

class Category(RowColumn):
    name = models.CharField(max_length=400)
    

class Items(RowColumn):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=400)


class TransactionType(RowColumn):
    name = models.CharField(max_length=400)
    description = models.CharField(max_length=400)


class SubInventoryTemp(RowColumn):
    item = models.ForeignKey(Items, on_delete=CASCADE)
    qty = models.IntegerField()
    

class Subinventory(RowColumn):
    item = models.ForeignKey(Items,on_delete=CASCADE)
    
    