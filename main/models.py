from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


# Manager for Custom User
class CustomUserManager(BaseUserManager):
    def _create_user(self, username, phone, password=None, **extra_fields):
        if not username or not phone:
            raise ValueError('The given username and phone must be set')
        
        user = self.model(username=username, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, phone, password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, phone, password,  **extra_fields)
        

    def create_superuser(self, username, phone, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, phone, password, **extra_fields)


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()
    