from django.db import models
from django.contrib.auth.models import User
# from Inventory.models import Items
from Party.models import Parties
# Create your models here.


class RowColumn(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(blank=False, null= False)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True ,related_name='%(class)s_created_by')
    Last_update_date = models.DateTimeField(auto_now=True)
    Last_update_by = models.IntegerField(blank=False, null= False)

    class Meta:
        abstract = True


class PriceListHeaders(RowColumn):
    price_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.price_name


class PriceListLines(RowColumn):
    header = models.ForeignKey(to='Sales.PriceListHeaders', on_delete=models.CASCADE)
    item = models.ForeignKey(to='Inventory.Items', on_delete=models.SET_NULL, null=True)
    value = models.IntegerField()


def upload_image(instance, image):
    imagename, imageexc = image.split('.')
    return 'Image/{}.{}'.format(instance.id, imageexc)


class Rooms(RowColumn):
    room_number = models.IntegerField()
    room_name = models.CharField(max_length=200)
    room_size = models.IntegerField()
    room_image = models.ImageField(upload_to=upload_image)

    def __str__(self) -> str:
        return self.room_name

discount = ((1, 'percentage'), (2, 'Amount'))
status = ((1, 'Entered'), (2, 'Booked'), (3, 'Canceled'), (4, 'Complete'))


class OrderHeaders(RowColumn):
    order_number = models.IntegerField()
    party = models.ForeignKey(Parties, on_delete=models.CASCADE)
    price_list = models.ForeignKey(PriceListHeaders, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    status = models.IntegerField(choices=status)
    discount_value = models.IntegerField()
    discount_type = models.IntegerField(choices=discount)
    total_order = models.IntegerField()

    def __str__(self) -> str:
        return self.order_number

class OrderLines(RowColumn):
    header = models.ForeignKey(OrderHeaders, on_delete=models.CASCADE)
    item = models.ForeignKey(to='Inventory.Items', on_delete=models.SET_NULL, null=True)
    price_list_line = models.ForeignKey(PriceListLines, on_delete=models.CASCADE)
    public_price = models.IntegerField()
    unit_selling_price = models.IntegerField()
    qty = models.IntegerField()
    wasted_flag = models.BooleanField()
    status = models.IntegerField(choices=status)
    discount_value = models.IntegerField()
    discount_type = models.IntegerField(choices=discount)


class InvoiceHeaders(RowColumn):
    invoice_number = models.IntegerField()
    party = models.ForeignKey(Parties, on_delete=models.CASCADE)
    price_list = models.ForeignKey(PriceListHeaders, on_delete=models.CASCADE)
    discount_value = models.IntegerField()
    discount_type = models.IntegerField(choices=discount)
    total_order = models.IntegerField()

    def __str__(self) -> str:
        return self.invoice_number

class InvoiceLines(RowColumn):
    header = models.ForeignKey(InvoiceHeaders, on_delete=models.CASCADE)
    order_header = models.ForeignKey(OrderHeaders, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    item = models.ForeignKey(to='Inventory.Items', on_delete=models.SET_NULL, null=True)
    price_list_line = models.ForeignKey(PriceListLines, on_delete=models.CASCADE)
    public_price = models.IntegerField()
    unit_selling_price = models.IntegerField()
    qty = models.IntegerField()
    discount_value = models.IntegerField()
    discount_type = models.IntegerField(choices=discount)
