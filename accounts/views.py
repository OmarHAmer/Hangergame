from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login as auth_login
from .models import NavBar
from .srp import *

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

            return render(request,'accounts/loginpage.html',context)

    else:

        loginform = AuthenticationForm()

        context = {
        'loginform':loginform
        }

        return render(request,'accounts/loginpage.html',context)


def navpage(request,app,slug):

    navdata = NavClass.mainbar()
    context = {
        **navdata
    }

    if app == 'None' :
        return render(request,slug+'.html',context)
    else:
        return render(request,app+'/'+slug+'.html',context)



def home(request):

    navdata = NavClass.mainbar()
    context = {
        **navdata
    }

    return render(request,'accounts/index.html',context)