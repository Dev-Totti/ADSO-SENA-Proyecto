from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def home(request):
    return HttpResponse("Hello, World!")


def temp(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, "core/temp.html", context)
