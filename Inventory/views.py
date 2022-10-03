from django.shortcuts import render
from .forms import FormItems
from accounts.models import NavBar
# Create your views here.

def master_items(request):

    data = NavBar.objects.all()
    bardata = data.filter(parent__isnull=True).order_by('order_by')
    childbardata = data.filter(parent__isnull=False).order_by('order_by')

    if request.method == 'POST':
        masterform = FormItems(request.POST)

        if masterform.is_valid():

            masterform = masterform.save(commit=False)
            masterform.save()
        
        else:
            masterform = FormItems(request.POST)
    else:
        masterform = FormItems({})
    
    context = {
        'bardata':bardata,
        'childbardata':childbardata,
        'masterform':masterform
    }

    return render(request,'Inventory/master-items.html',context)