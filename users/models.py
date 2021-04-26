from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class User(AbstractUser):
    """"Пользователи"""
    middle_name = models.CharField('Отчество', max_length=30, )
    phone = models.CharField('Номер телефона',  max_length=15, validators=[MinLengthValidator(11)],)
    address = models.CharField('Адрес', max_length=150)
    type_account = models.BooleanField('Премиум', default=False)
