from audioop import error

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from store.models import Category, Product
from django.db.models.functions import Cast


def home(request):
    products = Product.objects.all()
    par_categories = Category.objects.filter(parent__isnull=True)
    # if slug != None:
    #     products = products.filter(category__slug=slug)
    return render(request, 'index.html', {'products': products, 'par_categories': par_categories} )



def contact_view(request):
    return render(request, 'contact.html')

def category_listing(request, slug=None):
    tag = request.GET.get('tag', '')
    price = request.GET.get('rangeInput', '')
    tags = dict(Product.TAG_CHOICES)

    if slug:
        parent_category = get_object_or_404(Category, slug=slug)
        categories = parent_category.subcategoires.all()
        current_category = get_object_or_404(Category, slug=slug)
    else:
        categories = Category.objects.filter(parent__isnull=True)
        current_category = None

    products = Product.objects.all()
    if tag :
        products = products.filter(tag=tag)

    if price!='' and int(price)>0:
        products = products.filter(price__lte=price)

    sort = request.GET.get('sort', '')


    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'date_desc':
        products = products.order_by('-created_at')
    else:
        products = products.order_by('name')

    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    par_categories = Category.objects.filter(parent__isnull=True)
    if slug!=None:
        page_obj = products.filter(category__slug=slug)

    context = {
            'categories': categories,
            'products': page_obj,
            'par_categories': par_categories,
            'current_category': current_category,
            'tags': tags

        }
    return render(request, 'shop.html', context)

def product_detail(request):
    # product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop-detail.html', )

def testimonial(request):
    return render(request, 'testimonial.html')

def get404(request):
    return render(request, '404.html')