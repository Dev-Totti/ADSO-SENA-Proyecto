from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UserSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label='Nombre', required=True)
    last_name = forms.CharField(max_length=50, label='Apellido', required=True)
    email = forms.EmailField(max_length=254, label='Correo electrónico', required=True)
    password1 = forms.CharField(max_length=50, label='Contraseña', required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50, label='Confirmar contraseña', required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
