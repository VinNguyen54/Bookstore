from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.utils.text import slugify
from django.shortcuts import redirect, render

from .models import Vendor
from .forms import VendorLoginForm, ProductForm
from apps.product.models import Product

# Create your views here.
def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            vendor = Vendor.objects.create(name = user.username, created_by = user)

            mygroup = Group.objects.get(name = 'Vendor')
            mygroup.user_set.add(user)

            return redirect('vendor_admin')

    else:
        form = UserCreationForm()

    return render(request, 'vendor/become_vendor.html', {'form':form})


def vendor_login(request):

    if request.method == 'POST':
        form = VendorLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)

            login(request, user)

            group = Group(name = 'Vendor')

            if user.groups.filter(name = group):
                return redirect('vendor_admin')
            else:
                return ('vendor_login')

    else:
        form = VendorLoginForm()

    return render(request, 'vendor/login.html', {'form':form})

@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()

    return render(request, 'vendor/vendor_admin.html', {'vendor':vendor, 'products':products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.name)
            product.save()

            return redirect('vendor_admin')

    else:
        form = ProductForm()

    return render(request, 'vendor/add_product.html', {'form':form})