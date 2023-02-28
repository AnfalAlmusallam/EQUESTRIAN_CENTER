from django.contrib import admin
from .models import Club,Review,Booking,Contact,Comment
# Register your models here.
''' create admin panel to display all models  and its objects therefore whe can add and change data'''

class ClubAdmin(admin.ModelAdmin):
      list_display = ('image', 'club_name', 'club_services','feature','open_at','closed_at','price')

class ReviewAdmin(admin.ModelAdmin):
      list_display = ('club','content','rating','created_at')


class BookingAdmin(admin.ModelAdmin):
      list_display = ('club','initial_date_time','final_date_time')

class ContactAdmin(admin.ModelAdmin):
      list_display = ('first_name','last_name','email','msg')

class CommentAdmin(admin.ModelAdmin):
      list_display=('content',)


admin.site.register(Club, ClubAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)








