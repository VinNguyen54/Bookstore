from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='customer', on_delete=models.CASCADE)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username