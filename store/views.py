from django.shortcuts import render, get_object_or_404

from store.models import Category, Product
from django.db.models.functions import Cast


def home(request):
    return render(request, 'index.html')

def contact_view(request):
    return render(request, 'contact.html')

def category_listing(request):
    # category = get_object_or_404(Category, slug=slug)
    # products = category.products.all()
    return render(request, 'shop.html', )

def product_detail(request):
    # product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop-detail.html', )

def testimonial(request):
    return render(request, 'testimonial.html')

def get404(request):
    return render(request, '404.html')