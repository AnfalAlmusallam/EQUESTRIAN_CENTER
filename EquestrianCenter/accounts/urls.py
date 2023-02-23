from django.urls import path
from . import views

app_name ='accounts'

urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/",views.login_user,name="login_user"),
    path("welcome/",views.welcome_page,name="welcome_page"),
    path("loged_out/",views.loged_out,name="loged_out"),
    path("logout/",views.logout_user,name="logout_user"),
   
]