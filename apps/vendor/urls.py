from django.urls import path
from django.contrib.auth import views
from .views import become_vendor, vendor_admin, vendor_login

urlpatterns = [
    path('become-vendor/', become_vendor, name='become_vendor'),
    path('vendor-admin/', vendor_admin, name='vendor_admin'),

    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/',vendor_login, name='vendor_login'),
]