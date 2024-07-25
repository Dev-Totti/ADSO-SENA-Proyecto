from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from userauths.forms import UserSignupForm
from django.conf import settings

User = settings.AUTH_USER_MODEL


def signup_view(request):
    if request.user.is_authenticated:
        messages.info(request, "Ya has iniciado sesión")
        return redirect("core:index")

    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Nueva cuenta creada {username}')
            new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])

            login(request, new_user)
            messages.success(request, f'{username} se ha registrado correctamente')

            return redirect("core:index")
    else:
        form = UserSignupForm()

    context = {
        'form': form
    }

    return render(request, 'userauths/signup.html', context)


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "Ya has iniciado sesión")
        return redirect("core:index")

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect("core:index")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    context = {}

    return render(request, 'userauths/login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión")
    return redirect("core:index")
