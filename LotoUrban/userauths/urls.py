from django.urls import path
from userauths import views

app_name = 'userauths'

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("signin/", views.signin_view, name="signin"),
    path("signout/", views.signout_view, name="signout"),
]