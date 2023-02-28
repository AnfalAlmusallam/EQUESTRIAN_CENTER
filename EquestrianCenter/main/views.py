from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Club,Review,Booking,Contact,Comment
from django.contrib.auth.models import User
from datetime import datetime



'''define home_page to display home page , top clubs ,comment and fill the form conact for every one needs help '''

def home_page(request:HttpRequest):

    top_clubs=Review.objects.filter(rating__gte=4)
    comment= Comment.objects.all()

    if request.method == "POST":
        new_contact=Contact(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],msg=request.POST['msg'])
        new_contact.save()
        return redirect('main:success_contact')
    
    return render(request,"main/home.html", {"top_clubs" : top_clubs,"comment":comment})



''' create add_club_page to make team add clubs in this Center'''

def add_club_page(request:HttpRequest):
      if request.method == "POST":
        #to add a new entry
        new_club =Club(image= request.FILES["image"], club_name = request.POST["club_name"], club_services= request.POST["club_services"],feature=request.POST["feature"],open_at=request.POST["open_at"],closed_at=request.POST["closed_at"],price=request.POST["price"])
        new_club.save()

      return render(request, "main/add_club.html")

''' create update_club to make team update clubs in this Center'''

def update_club(request : HttpRequest, club_id):

    club= Club.objects.get(id=club_id)

    if request.method == "POST":
        club.club_name= request.POST["club_name"]
        club.club_services= request.POST["club_services"]
        club.feature= request.POST["feature"]
        club.open_at= request.POST["open_at"]
        club.closed_at= request.POST["closed_at"]
        club. price= request.POST["price"]
        #to check if user chosen a file to upload for the update
        if "image" in request.FILES:
            club.image = request.FILES["image"]

        club.save()
        return redirect("main:show_club_page")

    return render(request, "main/update_club.html", {"update": club})
    
'''delete clubs only team work can do that'''
def delete_club(request : HttpRequest, club_id):
   
    club=Club.objects.get(id=club_id)
    club.delete()
    return redirect("main:home_page")

'''create show_club_page to display the clubs for user'''

def show_club_page(request:HttpRequest):
    
    show_club= Club.objects.all()
    context={"show_club":show_club}

    return render(request,"main/show_club.html",context)

''' create club_detail to delete ,update and add reviews clubs from database'''

def club_detail(request : HttpRequest, club_id):

    club= Club.objects.get(id=club_id)
    reviews =Review.objects.filter(club=club)

    return render(request,"main/club_detail.html", {"club":club,"reviews":reviews})


'''create add_review ,club in the Review model equal to club in Club model'''

def add_review(request : HttpRequest,club_id):

    if request.method == "POST":
        club = Club.objects.get(id=club_id)
        new_review = Review(user= request.user,club=club, content = request.POST["content"],rating= request.POST['rating'],created_at=request.POST.get('created_at',False))
        new_review.save()

    return redirect("main:club_detail", club_id=club_id)

'''create book_detail to fill the form and complate booking '''

def book_detail(request : HttpRequest, club_id):

    club= Club.objects.get(id=club_id)
    book =Booking.objects.filter(club=club,user= request.user)
    
    return render(request,"main/book_detail.html", {"club":club,"book":book})

'''create check_available_date to check If someone has booking at the same time '''

def check_available_date(start_date : datetime , end_date :datetime) -> bool:
    if start_date == end_date:
        return True
    else:
        return False

def book_club(request : HttpRequest,club_id):

    if request.method == "POST":
        club = Club.objects.get(id=club_id)
        new_book=Booking(user= request.user,club=club,initial_date_time= request.POST["initial_date_time"], final_date_time=request.POST["final_date_time"])
        check_time= Booking.objects.filter(initial_date_time =request.POST['initial_date_time'],final_date_time=request.POST["final_date_time"])
        if check_time:
           return render(request,"main/apologize.html")
        
        
        else: 
           new_book.save()
           return redirect('main:success_book')
    return redirect("main:book_detail", club_id=club_id)


'''If the custumer book on date not available or time '''
def apologize_club(request:HttpRequest):
        return render(request,"main/apologize")

'''success booking'''
def success_book(request:HttpRequest):
    return render(request,"main/success_book.html")

'''success contact'''
def success_conact(request:HttpRequest):
    return render(request,"main/contact.html")



''' create add_comment to add Comment of Equestrain Center'''

def add_comment(request : HttpRequest):

    if request.method == "POST":
        comment= Comment.objects.all()
        new_comment =Comment(user= request.user, content = request.POST["content"])
        new_comment.save()

    return redirect("main:home_page")