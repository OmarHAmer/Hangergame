from django import forms
from .models import PriceListHeaders,PriceListLines,Rooms,OrderHeaders,OrderLines,InvoiceHeaders,InvoiceLines


class FormPriceListHeaders(forms.ModelForm):
    class Meta:
        model = PriceListHeaders
        fields = ['price_name']


class FormPriceListLines(forms.ModelForm):
    class Meta:
        model = PriceListLines
        fields = ['item','value']


class FormRooms(forms.ModelForm):
   class Meta:
        model = Rooms
        fields = ['room_number','room_name','room_size','room_image']


class FormOrderHeaders(forms.ModelForm):
    class Meta:
        model = OrderHeaders
        fields = ['order_number','party','price_list','room','status','discount_value','discount_type','total_order']


class FormOrderLines(forms.ModelForm):
    class Meta:
        model = OrderLines
        fields = ['item','price_list_line','public_price','unit_selling_price','qty','wasted_flag','discount_value','discount_type']


class FormInvoiceHeaders(forms.ModelForm):
    class Meta:
        model = InvoiceHeaders
        fields = '__all__'


class FormInvoiceLines(forms.ModelForm):
    class Meta:
        model = InvoiceLines
        fields = '__all__'