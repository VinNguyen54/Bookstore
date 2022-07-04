from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render

from .forms import SignupForm
from .models import Customer

# Create your views here.
def become_customer(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            customer = Customer.objects.create(name = user.username, email = user.email, created_by = user)

            mygroup = Group.objects.get(name = 'Customer')
            mygroup.user_set.add(user)

            return redirect('home')

    else:
        form = SignupForm()

    return render(request, 'customer/signup.html', {'form':form})