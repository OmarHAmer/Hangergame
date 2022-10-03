from django.shortcuts import render
from .forms import FormItems
from accounts.models import NavBar
from accounts.srp import NavClass
from .models import Items
# Create your views here.

def master_items(request):

    navdata = NavClass.mainbar()

    if request.method == 'POST':
        masterform = FormItems(request.POST)

        if masterform.is_valid():

            masterform = masterform.save(commit=False)
            masterform.save()
        
        else:
            masterform = FormItems(request.POST)
    else:
        masterform = FormItems({})
    
    item_type = Items.objects.all()
    context = {
        **navdata,
        'masterform':masterform,
        'item_type':item_type
        
    }

    return render(request,'Inventory/master-items.html',context)