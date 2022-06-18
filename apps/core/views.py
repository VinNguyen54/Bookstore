import re
from django.shortcuts import render

from apps.product.models import Product

# Create your views here.
def home(request):
    stand_products = Product.objects.all() [0:3]
    newest_products = Product.objects.all() [0:8]

    return render(request, 'core/home.html', {'newest_products':newest_products, 'stand_products':stand_products})

def contact(request):
    return render(request, 'core/contact.html')