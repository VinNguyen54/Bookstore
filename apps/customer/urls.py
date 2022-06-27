from django.urls import path
from .views import become_customer

urlpatterns = [
    path('become-customer/', become_customer, name='become_customer'),
]