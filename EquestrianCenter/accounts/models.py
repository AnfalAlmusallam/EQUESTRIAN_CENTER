from django.db import models
from django.contrib.auth.models import User


'''Create Class Profile for user to display her personal information and booking'''
class Profile(models.Model):

    #choices
    gender_choices = models.TextChoices("Gender", ["male", "female"])

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=64, choices=gender_choices.choices)
