from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


# Manager for Custom User
class CustomUserManager(BaseUserManager):
    def _create_user(self, username, phone, email, password=None, **extra_fields):
        if not username or not phone or not email:
            raise ValueError('The given username, phone and email must be set')
        
        user = self.model(username=username, phone=phone, email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, phone, email, password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, phone, email, password,  **extra_fields)
        

    def create_superuser(self, username, phone, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, phone, email, password, **extra_fields)


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=35, unique=True)
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['name', 'phone', 'email']

    objects = CustomUserManager()
    