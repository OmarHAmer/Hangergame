from django import forms
from .models import PriceListHeaders,PriceListLines,Rooms,OrderHeaders,OrderLines,InvoiceHeaders,InvoiceLines


class FormPriceListHeaders(forms.ModelForm):
    class Meta:
        model = PriceListHeaders
        fields = '__all__'


class FormPriceListLines(forms.ModelForm):
    class Meta:
        model = PriceListLines
        fields = '__all__'


class FormRooms(forms.ModelForm):
   class Meta:
        model = Rooms
        fields = ['room_number','room_name','room_size','room_image']


class FormOrderHeaders(forms.ModelForm):
    class Meta:
        model = OrderHeaders
        fields = '__all__'


class FormOrderLines(forms.ModelForm):
    class Meta:
        model = PriceListHeaders
        fields = '__all__'


class FormInvoiceHeaders(forms.ModelForm):
    class Meta:
        model = InvoiceHeaders
        fields = '__all__'


class FormInvoiceLines(forms.ModelForm):
    class Meta:
        model = InvoiceLines
        fields = '__all__'