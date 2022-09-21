from django.db import models
from django.contrib.auth.models import User
from Inventory.models import Items
from Party.models import Parties
# Create your models here.


class RowColumn(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(User, on_delete=models.CASCADE, blank=False)
    Last_update_date = models.DateTimeField(auto_now=True)
    Last_update_by = models.IntegerField(User, on_delete=models.CASCADE, blank=False)

    class Meta:
        abstract = True


class PriceListHeaders(RowColumn):
    price_name = models.CharField(max_length=200)


class PriceListLines(RowColumn):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    value = models.IntegerField()


def upload_image(instance, image):
    imagename, imageexc = image.split('.')
    return 'Image/{}.{}'.format(instance.id, imageexc)


class Rooms(RowColumn):
    room_number = models.IntegerField()
    room_name = models.CharField(max_length=200)
    room_size = models.IntegerField()
    room_image = models.ImageField(upload_to=upload_image)


discount = ((1, 'percentage'), (2, 'Amount'))
status = ((1, 'Entered'), (2, 'Booked'), (3, 'Canceled'), (4, 'Complete'))


class OrderHeaders(RowColumn):
    order_number = models.IntegerField()
    party = models.ForeignKey(Parties, on_delete=models.CASCADE)
    price_list = models.ForeignKey(PriceListHeaders, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=status)
    discount_value = models.IntegerField()
    discount_type = models.CharField(max_length=1, choices=discount)
    total_order = models.ImageField()


class OrderLines(RowColumn):
    header = models.ForeignKey(OrderHeaders, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    price_list_line = models.ForeignKey(PriceListLines, on_delete=models.CASCADE)
    public_price = models.IntegerField()
    unit_selling_price = models.IntegerField()
    qty = models.IntegerField()
    wasted_flag = models.CharField(max_length=1,null=True)
    status = models.CharField(max_length=1, choices=status)
    discount_value = models.IntegerField()
    discount_type = models.CharField(max_length=1, choices=discount)


class InvoiceHeaders(RowColumn):
    invoice_number = models.IntegerField()
    party = models.ForeignKey(Parties, on_delete=models.CASCADE)
    price_list = models.ForeignKey(PriceListHeaders, on_delete=models.CASCADE)
    discount_value = models.IntegerField()
    discount_type = models.CharField(max_length=1, choices=discount)
    total_order = models.ImageField()


class InvoiceLines(RowColumn):
    header = models.ForeignKey(InvoiceHeaders, on_delete=models.CASCADE)
    order_header = models.ForeignKey(OrderHeaders, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    price_list_line = models.ForeignKey(PriceListLines, on_delete=models.CASCADE)
    public_price = models.IntegerField()
    unit_selling_price = models.IntegerField()
    qty = models.IntegerField()
    discount_value = models.IntegerField()
    discount_type = models.CharField(max_length=1, choices=discount)
