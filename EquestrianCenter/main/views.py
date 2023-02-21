from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
'''define home_page to display home page '''
def home_page(request:HttpRequest):
      return render(request,"main/home.html")
def contact(request:HttpRequest):
      return render(request,"main/contact.html")