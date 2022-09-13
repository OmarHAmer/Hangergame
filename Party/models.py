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


PartyType = ((1, 'Customer'), (2, 'Supplier'))


class Parties(RowColumn):
    party_number = models.CharField(max_length=200)
    party_name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=12)
    address = models.CharField(max_length=400)
    party_type = models.CharField(max_length=1, choices=PartyType)
