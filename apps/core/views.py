from django.core.paginator import Paginator
from django.db.models import Q 
from django.shortcuts import render

from apps.product.models import Product, Category

# Create your views here.
def home(request):
    stand_products = Product.objects.all() [0:3]
    newest_products = Product.objects.all() [0:8]

    return render(request, 'core/home.html', {'newest_products':newest_products, 'stand_products':stand_products})

def shop (request):
    categories = Category.objects.all()
    products = Product.objects.all()

    # check category 
    active_category = request.GET.get('category', '')
    if active_category:
        products = products.filter(category__slug = active_category)

    query = request.GET.get('query', '')
    if query:
        products = products.filter(Q(name__icontains = query) | Q(desciption__icontains = query))


    # paginator 
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/shop.html', {'page_obj':page_obj, 'categories':categories, 'active_category':active_category})

def contact(request):
    return render(request, 'core/contact.html')