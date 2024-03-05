from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager) :
    def create_user(self,email,password,**extra_fields):
        if not email : raise ValueError('email must be set')
        if not password : raise ValueError('password must be set')
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        if not extra_fields.get("is_active") : raise ValueError('superuser must have is_active=True')
        if not extra_fields.get("is_staff") : raise ValueError('superuser must have is_staff=True')
        if not extra_fields.get("is_superuser") : raise ValueError('superuser must have is_superuser=True')
        return self.create_user(email,password,**extra_fields)