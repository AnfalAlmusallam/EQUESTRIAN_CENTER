from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from main.models import Club,Booking


# Create your views here.

'''create user '''
def register_user(request:HttpRequest):
    if request.method=="POST":
       
       new_user=User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
       new_user.save()

       '''Creating the profile'''
       user_profile = Profile(user=new_user, birth_date=request.POST["birth_date"], gender=request.POST["gender"])
       user_profile.save()

        #if register successful redirect to sign in page
       return redirect("accounts:login_user")
    return render(request,"accounts/register.html")

def login_user(request:HttpRequest):
    loggin_msg = None
    if request.method=="POST":
        user=authenticate(request,username=request.POST["username"],password=request.POST["password"])
        if user is not None:
            login(request,user)
            return redirect("accounts:welcome_page")
        else:
             loggin_msg = "Please Use correct Credentials"

    return render(request, "accounts/login.html", {"msg" : loggin_msg})

def welcome_page(reqest:HttpRequest):
    return render(reqest,"accounts/welcome.html")


def logout_user(request : HttpRequest):

    logout(request)

    return redirect("main:home_page")

def loged_out(request:HttpRequest):
    return render(request,"accounts/logout.html")


def profile_user(request : HttpRequest):

    book= Booking.objects.filter(user=request.user.id)

    return render(request,"accounts/profile.html",{"book":book})

 