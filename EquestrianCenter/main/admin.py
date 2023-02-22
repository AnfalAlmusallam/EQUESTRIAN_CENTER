from django.contrib import admin
from .models import Club
# Register your models here.
''' create admin panel to display all models  and its objects therefore whe can add and change data'''

class ClubAdmin(admin.ModelAdmin):
    list_display = ('image', 'club_name', 'club_services','price')



admin.site.register(Club, ClubAdmin)

