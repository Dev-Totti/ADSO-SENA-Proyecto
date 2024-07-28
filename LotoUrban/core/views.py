from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, "index.html", context)


def temp(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, "core/temp.html", context)

def test(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, "test/index.html", context)
