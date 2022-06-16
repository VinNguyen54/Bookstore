from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate

from apps.product.models import Product

class VendorLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)

            if not user:
                raise forms.ValidationError('User does not exits')

            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')

        return super(VendorLoginForm, self).clean(*args, **kwargs)


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'name', 'desciption', 'price', 'author', 'page', 'publisher', 'publish_date']