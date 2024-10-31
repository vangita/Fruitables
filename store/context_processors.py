from store.models import Category, Product

def global_context(request):
    context = {
        'par_categories': Category.objects.filter(parent__isnull=True),
        'tags': dict(Product.TAG_CHOICES),
        'cart_count': request.session.get('cart_count', 0),
        'user' : request.user,
    }
    return context
