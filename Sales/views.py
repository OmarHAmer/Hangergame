from django.urls import reverse
from django.shortcuts import render,redirect
from accounts.srp import NavClass
from .forms import FormPriceListHeaders,FormPriceListLines,FormRooms,FormOrderHeaders,FormOrderLines,FormInvoiceHeaders,FormInvoiceLines
from .models import Rooms,PriceListLines,OrderLines
from django.contrib.auth.models import User
# Create your views here.


def rooms(request):

    navbar  = NavClass.mainbar()

    if request.method == 'POST' :

        formrooms = FormRooms(request.POST,request.FILES)

        if formrooms.is_valid():

            formrooms.cleaned_data
            formrooms = formrooms.save(commit=False)
            formrooms.created_by = request.user.id
            formrooms.Last_update_by = request.user.id
            formrooms.save()
            return redirect(reverse('Sales:displayrooms'))
        
        else:

            formrooms = FormRooms(request.POST,request.FILES)

            context = {
                **navbar,
                'formrooms':formrooms,
            }
        
        return render(request,'Sales/create-room.html',context)

    else:

        formrooms = FormRooms({})

        context = {
            **navbar,
            'formrooms':formrooms,
        }
    
    return render(request,'Sales/create-room.html',context)


def displayrooms(request):

    navbar  = NavClass.mainbar()
    roomsdata = Rooms.objects.all()
    
    context = {
                **navbar,
                'roomsdata':roomsdata
            }
    return render(request,'Sales/room-data.html',context)


def createprice(request):

    navbar  = NavClass.mainbar()

    if request.method == 'POST':
    
        formprice = FormPriceListHeaders(request.POST)

        if formprice.is_valid():

            formprice.cleaned_data
            formprice = formprice.save(commit=False)
            formprice.created_by = request.user.id
            formprice.Last_update_by = request.user.id
            formprice.save()
            return redirect(reverse('Sales:displaypricelist'))
        
        else:

            context = {
                **navbar,
                'formprice':formprice,
            }
        
        return render(request,'Sales/create-price-list.html',context)

    else:

        formprice = FormPriceListHeaders({})
        context = {
                **navbar,
                'formprice':formprice,
            }
        return render(request,'Sales/create-price-list.html',context)


def displaypricelist(request):

    navbar  = NavClass.mainbar()
    pricelistdata = PriceListLines.objects.all()

    context = {
        **navbar,
        'pricelistdata':pricelistdata
    }

    return render(request,'Sales/price-list-data.html',context)


def createorder(request):

    navbar  = NavClass.mainbar()

    if request.method == 'POST':
    
        formorder = FormOrderHeaders(request.POST)

        if formorder.is_valid():

            formorder.cleaned_data
            formorder = formorder.save(commit=False)
            formorder.created_by = request.user.id
            formorder.Last_update_by = request.user.id
            formorder.save()
            return redirect(reverse('Sales:displayorder'))
        
        else:

            context = {
                **navbar,
                'formorder':formorder,
            }
        
        return render(request,'Sales/create-order.html',context)

    else:

        formorder = FormOrderHeaders({})
        context = {
                **navbar,
                'formorder':formorder,
            }
        return render(request,'Sales/create-order.html',context)


def displayorder(request):

    navbar  = NavClass.mainbar()
    orderdata = OrderLines.objects.all()

    context = {
        **navbar,
        'orderdata':orderdata
    }

    return render(request,'Sales/order-data.html',context)