from django.db import models

# Create your models here.
'''Create class named Club and its objects '''
class Club(models.Model):

    image= models.ImageField(upload_to="images/%y/%m/%d")
    club_name= models.CharField(max_length=10)
    club_services= models.TextField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    time_open_closed=models.TimeField()