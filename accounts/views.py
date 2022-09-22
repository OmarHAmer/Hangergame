from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login

def login(request):

    if request.method == 'POST':
        
        loginform = AuthenticationForm(data=request.POST)

        if loginform.is_valid():

            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password1']
            user = authenticate(username=username,password=password) 

            if user :
                login(request,user)
                return redirect(reverse('accounts:Home'))

    else:

        loginform = AuthenticationForm()

        context = {
        'loginform':loginform
        }

        return render(request,'loginpage.html',context)


def home(request):

    context = {

    }

    return render(request,'index.html',context)