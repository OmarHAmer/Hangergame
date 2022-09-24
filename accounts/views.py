from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login as auth_login
from .models import NavBar


def login(request):

    if request.method == 'POST':
        
        loginform = AuthenticationForm(data=request.POST)
        print ("from loginform")
        if loginform.is_valid():

            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']
            user = authenticate(request,username=username,password=password) 

            if user :
                auth_login(request,user)
                return redirect(reverse('accounts:Home'))
        else:

            loginform = AuthenticationForm(data=request.POST)

            context = {
            'loginform':loginform
            }

            return render(request,'loginpage.html',context)

    else:

        loginform = AuthenticationForm()

        context = {
        'loginform':loginform
        }

        return render(request,'loginpage.html',context)


def navbar(request):
    pass
    



def home(request):

    bardata = NavBar.objects.all()

    context = {
        bardata:bardata
    }

    return render(request,'index.html',context)