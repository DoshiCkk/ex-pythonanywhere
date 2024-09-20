from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SighUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'birthday', 'picture', 'address']
