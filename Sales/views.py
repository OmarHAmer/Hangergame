from django.urls import reverse
from django.shortcuts import render,redirect
from accounts.srp import NavClass
from .forms import FormPriceListHeaders,FormPriceListLines,FormRooms,FormOrderHeaders,FormOrderLines,FormInvoiceHeaders,FormInvoiceLines
from .models import Rooms
from django.contrib.auth.models import User
# Create your views here.


def rooms(request):

    navbar  = NavClass.mainbar()

    if request.method == 'POST' :

        formrooms = FormRooms(request.POST,request.FILES)


        if formrooms.is_valid():
            print(request.user.id)
            formrooms.cleaned_data
            formrooms.save(commit=False)
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