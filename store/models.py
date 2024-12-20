from django.db import models
from versatileimagefield.fields import VersatileImageField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey('self',  on_delete=models.CASCADE, null=True, blank=True, related_name='subcategoires')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    TAG_CHOICES = [
        ('Fresh','fresh'),
        ('On Sale','on_sale'),
        ('Organic','organic'),
        ('Best Seller','best_seller'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    slug = models.SlugField(max_length=100, unique=True)
    tag = models.CharField(max_length=255, choices=TAG_CHOICES, null=True)
    image = VersatileImageField(upload_to='products/', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    is_in_stock = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name