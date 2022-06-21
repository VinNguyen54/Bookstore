from django.urls import path
from .views import product

urlpatterns = [
    path('<slug:slug>/', product, name='product'),
]