from django.contrib import admin
from .models import Club,Review,Booking
# Register your models here.
''' create admin panel to display all models  and its objects therefore whe can add and change data'''

class ClubAdmin(admin.ModelAdmin):
      list_display = ('image', 'club_name', 'club_services','price')


class ReviewAdmin(admin.ModelAdmin):
      list_display = ('club','content','rating','image','created_at')


class BookingAdmin(admin.ModelAdmin):
      list_display = ('club','initial_time','final_time')


admin.site.register(Club, ClubAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Booking, BookingAdmin)




