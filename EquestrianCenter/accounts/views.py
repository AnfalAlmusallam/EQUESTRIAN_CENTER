from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

'''create user '''
def register_user(request:HttpRequest):
    if request.method=="POST":
       new_user=User.objects.create_user(username=request.POST["username"],email=request.POST["email"],password=request.POST["password"])
       new_user.save()
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

    return redirect("hospital:home_page")

def loged_out(request:HttpRequest):
    return render(request,"accounts/logout.html")