from django.urls import path
from .views import checkout_view , cart_view

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
]