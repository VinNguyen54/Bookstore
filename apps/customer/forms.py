from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class':'box',
            'type' : 'text',
            'placeholder': 'enter your username',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'box',
            'type' : 'email',
            'placeholder': 'enter your email',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'box',
            'type': 'password',
            'placeholder': 'password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'box',
            'type': 'password',
            'placeholder': 'repassword'
        })


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    