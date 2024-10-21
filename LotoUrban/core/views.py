from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, "index.html", context)


def full(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, "full/index.html", context)
