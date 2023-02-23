from django.urls import path
from .import views

app_name="main"

urlpatterns =[
    path('',views.home_page, name='home_page'),
    path('add_club/',views.add_club_page,name='add_club_page'),
    path("update_club/<club_id>/",views.update_club,name="update_club"),
    path("show_club/",views.show_club_page,name="show_club_page"),
    path("review/add/<club_id>/", views.add_review,name="add_review"),
    path("details/<club_id>/", views.club_detail,name="club_detail"),
    path("delete/club/<club_id>/",views.delete_club,name="delete_club"),


]