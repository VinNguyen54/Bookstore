from django.urls import path
from .views import become_customer

urlpatterns = [
    path('signup/', become_customer, name='signup'),
]