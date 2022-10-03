from .models import *


class NavClass:

    def __init__(self):
        pass

    def mainbar():

        data = NavBar.objects.all()
        bardata = data.filter(parent__isnull=True).order_by('order_by')
        childbardata = data.filter(parent__isnull=False).order_by('order_by')

        context={
            'bardata':bardata,
            'childbardata':childbardata,
        }
        return context