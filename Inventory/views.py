from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from .forms import FormItems
from accounts.models import NavBar
from accounts.srp import NavClass
from .models import Items, Category
# Create your views here.

def master_items(request):

    navdata = NavClass.mainbar()
    print(request.POST)
    if request.method == 'POST':
        masterform = FormItems(request.POST)

        if masterform.is_valid():
            masterform.cleaned_data
            masterform = masterform.save(commit=False)
            masterform.created_by = request.user.id
            masterform.Last_update_by = request.user.id
            masterform.save()
            return redirect(reverse('Inventory:displayitems'))
        
        else:
            masterform = FormItems(request.POST)

            context = {
                **navdata,
                'masterform':masterform,
            }

            return render(request,'Inventory/master-items.html',context)

    else:
        masterform = FormItems({})
    
    context = {
        **navdata,
        'masterform':masterform,
        
    }

    return render(request,'Inventory/master-items.html',context)


def displayitems(request):

    navdata = NavClass.mainbar()

    itemsdata = Items.objects.all()

    context = {
        **navdata,
        'itemsdata':itemsdata,
    }

    return render(request,'Inventory/items-data.html',context)

@csrf_protect
def creatcatfromitems(request):
    
    if request.method == 'POST':

        category = request.POST['name']
        catinsert = Category.objects.create(name = category, created_by= request.user.id,Last_update_by= request.user.id)
        context= str(catinsert.id) + ":" + catinsert.name

        return HttpResponse(context)
    
    else:

        return False
        