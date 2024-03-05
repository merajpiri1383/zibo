from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.crypto import get_random_string
from user.manager import UserManager
class User(AbstractBaseUser,PermissionsMixin) :
    email = models.EmailField(max_length=200,unique=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    activation_code = models.SlugField(null=True,blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return self.email
    def save(self,**kwargs):
        self.activation_code = get_random_string(30)
        return super().save(**kwargs)