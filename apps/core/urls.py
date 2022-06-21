from django.urls import path
from .views import home, contact, shop
from apps.product.views import product

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact' ),
    path('shop/',shop, name = 'shop'),
    path('product/', product, name='product'),
]