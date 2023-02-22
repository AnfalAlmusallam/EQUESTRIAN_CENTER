from django.db import models

# Create your models here.
'''Create class named Club and its objects '''
class Club(models.Model):

    PRICE_CHOICES=models.TextChoices('price',['50$','100$','200$','300$'])

    image= models.ImageField(upload_to="images/%y/%m/%d")
    club_name= models.CharField(max_length=10)
    club_services= models.TextField()
    price= models.CharField(max_length=300,choices=PRICE_CHOICES.choices)
