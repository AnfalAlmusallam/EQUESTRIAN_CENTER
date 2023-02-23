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

'''Create class named Comment and its objects '''

class Review(models.Model):
    club=models.ForeignKey(Club,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    rating=models.FloatField()
    image= models.ImageField(upload_to="profile_pic",default='default.jpg')
    created_at=models.DateTimeField(auto_now_add=True)
