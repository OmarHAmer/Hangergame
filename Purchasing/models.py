from django.db import models
from django.contrib.auth.models import User
# from Inventory.models import Items
# from django.apps import apps
# Items = apps.get_model('Inventory.Items')
from Party.models import Parties
# Create your models here.


class RowColumn(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(User, blank=False, null= False)
    Last_update_date = models.DateTimeField(auto_now=True)
    Last_update_by = models.IntegerField(User, blank=False, null= False)

    class Meta:
        abstract = True


status = ((1, 'Entered'), (2, 'Approve'), (3, 'Canceled'), (4, 'Close'))


class PurchaseHeaders(RowColumn):
    po_number = models.IntegerField()
    party = models.ForeignKey(Parties, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=status)
    total_purchase = models.ImageField()


class PurchaseLines(RowColumn):
    header = models.ForeignKey(PurchaseHeaders, on_delete=models.CASCADE)
    item = models.ForeignKey(to='Inventory.Items', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    qty = models.IntegerField()
    status = models.CharField(max_length=1, choices=status)
