from django.shortcuts import render, redirect, HttpResponse 
from .forms import *
from django.contrib.auth import get_user, logout,login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# # Create your views here.
def index(request):
    return render(request, "Registration_Module/index.html")

def register_user(request):

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registration successful." )
        
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")


    form = NewUserForm()
    return render (request, "Registration_Module/register.html", context={"register_form":form})


def register_hospital_staff(request):

    if request.method == 'POST':
        form = HospitalUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            HospitalStaff.objects.create(user=user)
            login(request,user)
            messages.success(request, "Registration successful." )
        
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")


    form = HospitalUserForm()
    return render (request, "Registration_Module/register.html", context={"register_form":form})


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {email}.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    form = AuthenticationForm()
    return render(request,'Registration_Module/login.html',context={"login_form":form})   


def signout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('/')

