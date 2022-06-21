import random

from django.shortcuts import render,get_object_or_404

from .models import Product, Category

# Create your views here.

def product(request, slug):
    product = Product.objects.get(slug = slug)

    similar_products = list(product.category.products.exclude(id = product.id))

    if len(similar_products) >=4:
        similar_products = random.sample(similar_products, 4)

    return render(request, 'product/product.html', {'product':product, 'similar_products':similar_products})
   