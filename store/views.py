from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import Paginator
from store.models import Category, Product


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['par_categories'] = Category.objects.filter(parent__isnull=True)
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'


from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from store.models import Category, Product


class CategoryListingView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = Product.objects.all()
        tag = self.request.GET.get('tag', '')
        price = self.request.GET.get('rangeInput', '')
        search = self.request.GET.get('q', '')

        if search:
            queryset = queryset.filter(name__icontains=search)

        if tag:
            queryset = queryset.filter(tag=tag)
        if price and int(price) > 0:
            queryset = queryset.filter(price__lte=price)

        sort = self.request.GET.get('sort', '')
        if sort == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort == 'price_desc':
            queryset = queryset.order_by('-price')
        elif sort == 'date_desc':
            queryset = queryset.order_by('-created_at')

        slug = self.kwargs.get('slug')
        if slug:
            queryset = queryset.filter(category__slug=slug)

        return queryset

    def post(self, request, *args, **kwargs):
        if 'cart_count' not in request.session:
            request.session['cart_count'] = 0
        request.session['cart_count'] += 1
        request.session.modified = True

        return redirect(request.path)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        if slug:
            context['parent_category'] = get_object_or_404(Category, slug=slug)
            context['categories'] = context['parent_category'].subcategoires.all()
            context['current_category'] = context['parent_category']
        else:
            context['categories'] = Category.objects.filter(parent__isnull=True)
            context['current_category'] = None
        context['par_categories'] = Category.objects.filter(parent__isnull=True)
        context['tags'] = dict(Product.TAG_CHOICES)

        context['cart_count'] = self.request.session.get('cart_count', 0)
        return context


class ProductDetailView(TemplateView):
    template_name = 'shop-detail.html'


class TestimonialView(TemplateView):
    template_name = 'testimonial.html'


class Custom404View(TemplateView):
    template_name = '404.html'
