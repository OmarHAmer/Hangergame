from django.db import models
from django.contrib.auth.models import User
from Purchasing.models import PurchaseHeaders, PurchaseLines
from Sales.models import OrderHeaders, OrderLines

class RowColumn(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(User, blank=False, null= False)
    Last_update_date = models.DateTimeField(auto_now=True)
    Last_update_by = models.IntegerField(User, blank=False, null= False)

    class Meta:
        abstract = True
        

class Category(RowColumn):
    name = models.CharField(max_length=400)
    
itemtype = ((1,'Row Material'),(2,'Finished Goods'),(3,'Game'))

class Items(RowColumn):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=400)
    item_type = models.IntegerField(choices=itemtype)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    order_flag = models.CharField(max_length=1)
    batch_flag = models.CharField(max_length=1)
    complete_flag = models.CharField(max_length=1)

class BatchHeaders(RowColumn):
    code = models.CharField(max_length=10)
    active_flag = models.CharField(max_length=1)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    max_production = models.IntegerField()


class BatchLines(RowColumn):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    batch_header = models.ForeignKey(BatchHeaders,on_delete=models.CASCADE)
    qty = models.IntegerField()


class Subinventory(RowColumn):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=400)


transactiontype = ((1,'Dept Transaction'),(2,'Credit Transaction'))

class TransactionsTemp(RowColumn):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    qty = models.IntegerField()
    subinventory = models.ForeignKey(Subinventory,on_delete=models.CASCADE)
    transaction_type = models.IntegerField(choices=transactiontype)
    batch_header = models.ForeignKey(BatchHeaders,on_delete=models.CASCADE)
    purchase_header = models.ForeignKey(PurchaseHeaders,on_delete=models.SET_NULL, null=True)
    purchase_Line = models.ForeignKey(PurchaseLines,on_delete=models.SET_NULL, null=True)
    order_header = models.ForeignKey(OrderHeaders,on_delete=models.SET_NULL, null=True)
    order_line = models.ForeignKey(OrderLines,on_delete=models.SET_NULL, null=True)

class Transactions(RowColumn):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    qty = models.IntegerField()
    subinventory = models.ForeignKey(Subinventory,on_delete=models.CASCADE)
    transaction_type = models.IntegerField(choices=transactiontype)
    batch_header = models.ForeignKey(BatchHeaders,on_delete=models.CASCADE)
    purchase_header = models.ForeignKey(PurchaseHeaders,on_delete=models.SET_NULL, null=True)
    purchase_Line = models.ForeignKey(PurchaseLines,on_delete=models.SET_NULL, null=True)
    order_header = models.ForeignKey(OrderHeaders,on_delete=models.SET_NULL, null=True)
    order_line = models.ForeignKey(OrderLines,on_delete=models.SET_NULL, null=True)
