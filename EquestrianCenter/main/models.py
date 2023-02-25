from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''Create class named Club and its objects '''
class Club(models.Model):

    PRICE_CHOICES=models.TextChoices('price',['50$','100$','200$','300$'])
    

    image= models.ImageField(upload_to="images/%y/%m/%d")
    club_name= models.CharField(max_length=10)
    club_services= models.TextField()
    price= models.CharField(max_length=300,choices=PRICE_CHOICES.choices)

    def __str__(self) -> str:
        return f"{self.club_name}"
    def __str__(self) -> str:
        return f"{self.club_services}"
    
    
'''Create class Booking and its objects for user to book club '''

class Booking(models.Model):
    club=models.ForeignKey(Club,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    initial_time=models.TimeField()
    final_time=models.TimeField()

    def __str__(self) -> str:
        return f"{self.club} "



'''Create class named Review and its objects to review and rate clubs '''

class Review(models.Model):
    club=models.ForeignKey(Club,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    rating=models.FloatField()
    image= models.ImageField(upload_to="profile_pic",default='default.jpg')
    created_at=models.DateTimeField(auto_now_add=True)

'''Create class named Contact nd its objects to contact with client'''
'''using  pip install django-phone-field for phone number '''

class Contact(models.Model):
     first_name=models.CharField(max_length=50)
     last_name=models.CharField(max_length=50)
     email=models.EmailField(max_length=50)
     msg=models.TextField()


    
