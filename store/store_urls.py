from xml.sax import parse

from django.urls import path
from .views import home, contact_view, category_listing, product_detail, testimonial, get404

urlpatterns = [
    path('', home, name='home'),
    path('product/', product_detail, name='product_detail'),
  # path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('contact/',contact_view, name='contact'),
    path('category/', category_listing, name='generic_category_listing'),
    path('category/<slug:slug>/', category_listing , name='category_listing'),
    path('testimonial/', testimonial, name='testimonial'),
    path('404/', get404 , name='get404'),
]