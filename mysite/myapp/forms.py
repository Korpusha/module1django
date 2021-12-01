from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer


class SignUpForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = [
            'username',
            'password1',
            'password2',
        ]
