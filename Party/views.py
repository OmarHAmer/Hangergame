from django.urls import reverse
from django.shortcuts import render,redirect
from .forms import PartiesForm
from .models import Parties
from accounts.srp import NavClass
from django.contrib.auth.models import User
# Create your views here.

def parties(request):

    navbar  = NavClass.mainbar()

    if request.method == 'POST':

        partiesform = PartiesForm(request.POST)

        if partiesform.is_valid():

            partiesform.cleaned_data
            partiesform = partiesform.save(commit=False)
            partiesform.created_by = request.user.id
            partiesform.Last_update_by = request.user.id
            partiesform.save()
            return redirect(reverse('Party:displayparties'))

        else:

            # print(request.POST)
            partiesform = PartiesForm(request.POST)

            context = {
                **navbar,
                'partiesform':partiesform,
            }

            return render(request,'Party/create-parties.html',context)
    else:
        partiesform = PartiesForm({})

        context = {
            **navbar,
            'partiesform':partiesform,
        }

        return render(request,'Party/create-parties.html',context)


def displayparties(request):

    navbar  = NavClass.mainbar()
    # with connection.cursor() as cursor:
    #     cursor.execute('''SELECT * from party_parties;''')
    #     columns = [col[0] for col in cursor.description]
    #     data = [
    #                 dict(zip(columns, row))
    #                 for row in cursor.fetchall()
    #             ]


    partiesdata = Parties.objects.all()
    # columns = [f.name for f in Parties._meta.get_fields(include_parents=False, include_hidden=True)] 
    context = {
                **navbar,
                'partiesdata':partiesdata
            }
    return render(request,'Party/parties-data.html',context)