from django.urls import path
from userauths import views

app_name = 'userauths'

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("signin/", views.signin_view, name="signin"),
    path("signout/", views.signout_view, name="signout"),
    path("tempsignup/", views.temp_signup_view, name="tempsignup"),
    path("tempsignin/", views.temp_signin_view, name="tempsign"),
    path("tempsignout/", views.temp_signout_view, name="tempsignout"),
]