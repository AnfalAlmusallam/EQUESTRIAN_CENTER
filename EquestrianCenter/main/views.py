from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Club

'''define home_page to display home page '''

def home_page(request:HttpRequest):
      return render(request,"main/home.html")

''' create add_club_page to make teams add clubs in this Center'''
def add_club_page(request:HttpRequest):
      if request.method == "POST":
        #to add a new entry
        new_club =Club(image= request.FILES["image"], club_name = request.POST["club_name"], club_services= request.POST["club_services"], price=request.POST["price"])
        new_club.save()

      return render(request, "main/add_club.html")

'''create show_club_page to display the clubs for user'''
def show_club_page(request:HttpRequest):
     
    show_club = Club.objects.all()

    context = {"show" : show_club}
    return render(request, "main/show_club.html", context)


