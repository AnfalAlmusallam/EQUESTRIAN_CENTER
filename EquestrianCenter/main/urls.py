from django.urls import path
from .import views

app_name="main"

urlpatterns =[
    path('home/',views.home_page, name='home_page'),
    path('add_club/',views.add_club_page,name='add_club_page'),
    path('show_club/',views.show_club_page,name='show_club_page'),
]