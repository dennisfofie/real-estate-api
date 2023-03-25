from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_kwargs):
        user = self.model(
            username=username, email=self.normalize_email(email), **extra_kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_kwargs):
        user = self.create_user(username=username, email=email, **extra_kwargs)
        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique=True, db_index=True)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    profile = models.ImageField(upload_to="images/profile_pic/", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = CustomUserManager()

    def __str__(self):
        return self.username
