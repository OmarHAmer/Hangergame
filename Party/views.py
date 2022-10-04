from multiprocessing import context
from django.shortcuts import render
from .forms import PartiesForm
from accounts.srp import NavClass
# Create your views here.

def parties(request):

    navbar  = NavClass.mainbar()

    if request.method == 'POST':

        partiesform = PartiesForm(request.POST)

        if partiesform.is_valid():

            partiesform = partiesform.save(commit=False)
            partiesform = partiesform.cleaned_data
            partiesform.save()
            

        else:

            partiesform = PartiesForm(request.POST)

            context = {
                **navbar,
                'partiesform':partiesform
            }

            return render(request,'Party/create-parties.html',context)
    else:
        partiesform = PartiesForm({})

        context = {
            **navbar,
            'partiesform':partiesform,
        }

        return render(request,'Party/create-parties.html',context)

