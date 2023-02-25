from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Club,Review,Booking,Contact
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from django.core.mail import BadHeaderError,send_mail



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

def update_club(request : HttpRequest, club_id):

    club= Club.objects.get(id=club_id)
    if request.method == "POST":
        club.club_name = request.POST["club_name"]
        club.club_services = request.POST["club_services"]
        club. price= request.POST["price"]
        #to check if user chosen a file to upload for the update
        if "image" in request.FILES:
            club.image = request.FILES["image"]

        club.save()
        return redirect("main:show_club_page")

    return render(request, "main/update_club.html", {"update": club})
    

def delete_club(request : HttpRequest, club_id):
   
    club=Club.objects.get(id=club_id)
    club.delete()
    return redirect("main:home_page")

'''create show_club_page to display the clubs for user'''
def show_club_page(request:HttpRequest):
    
    show_club= Club.objects.all()
    context={"show_club":show_club}

    return render(request,"main/show_club.html",context)

''' create club_detail to delete and update clubs from database and add reviews'''
def club_detail(request : HttpRequest, club_id):

    club= Club.objects.get(id=club_id)
    reviews =Review.objects.filter(club=club)

    return render(request,"main/club_detail.html", {"club":club,"reviews":reviews})


'''club in the Review model equal to club in Club model'''

def add_review(request : HttpRequest,club_id):

    if request.method == "POST":
        club = Club.objects.get(id=club_id)
        new_review = Review(user= request.user,club=club, content = request.POST["content"],rating= request.POST.get('rating',False),created_at=request.POST.get('created_at',False))
        new_review.save()

    return redirect("main:club_detail", club_id=club_id)

def book_detail(request : HttpRequest, club_id):

    club= Club.objects.get(id=club_id)
    book =Booking.objects.filter(club=club,user= request.user)
    
    return render(request,"main/book_detail.html", {"club":club,"book":book})

def check_availbal_date(date1 : datetime , date2 :datetime) -> bool:
    if date1 == date2:
        return True
    else:
        return False
    

def book_club(request : HttpRequest,club_id):

    if request.method == "POST":
        club = Club.objects.get(id=club_id)
        new_book=Booking(user= request.user,club=club,initial_time= request.POST["initial_time"], final_time=request.POST["final_time"])
        check_time= Booking.objects.filter(initial_time =request.POST['initial_time'],final_time=request.POST["final_time"])
        
        if check_time :
           return render(request,"main/apologize.html")


        else: 
           new_book.save()
           return redirect('main:home_page')


        
    return redirect("main:book_detail", club_id=club_id)
 

def contact(request:HttpRequest):
    if request.method=="POST":
        contact=Contact(request.POST)
        if contact:
            subject="Website Inquiry"
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            email=request.POST.get('email')
            msg=request.POST.get('msg')
            
   
        try:
            send_mail(subject,'anfal.ame9@gmail.com',['anfal.ame8@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found ')
        return redirect("main:home_page")
    form=contact()
    return render(request,"main/home.html",{'form':form})


'''Create top_clubs based on rating'''
def top_clubs(request:HttpRequest):
    top_clubs= Club.objects.filter(rating__gte=4)

    context = {"top_clubs" : top_clubs}
    return render(request, "main/top_club.html", context)








