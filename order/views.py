from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def checkout_view(request):
    return render(request, 'checkout.html')


def cart_view(request):
    return render(request, 'cart.html')