from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birthday = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name='Адрес', null=True, blank=True)
    picture = models.ImageField(upload_to='profile_pics', verbose_name='Аватар', null=True, blank=True)
