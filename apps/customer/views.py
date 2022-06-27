from multiprocessing import reduction
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render


from .forms import CustomerRegisterForm
from .models import Customer

def become_customer(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            customer = Customer.objects.create(username = user.username, email = user.email, created_by = user)

            mygroup = Group.objects.get(name = 'Customer')
            mygroup.user_set.add(user)

            return redirect('home')

    else:
        form = CustomerRegisterForm()

    return render(request, 'customer/become_customer.html', {'form':form})