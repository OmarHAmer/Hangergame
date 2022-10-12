from django.contrib import admin
from .models import Rooms,PriceListLines,PriceListHeaders
# Register your models here.

admin.site.register(Rooms)
admin.site.register(PriceListHeaders)
admin.site.register(PriceListLines)