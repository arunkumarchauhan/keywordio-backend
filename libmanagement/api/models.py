from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(**extra_fields)
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.email = email
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, password, **extra_fields):
        user = self._create_user(password=password, is_staff=True, is_superuser=True, **extra_fields)
        return user

    def get_queryset(self):
        return super(CustomUserManager, self).get_queryset()


class User(AbstractBaseUser, TimeStampModel, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    # objects_all = models.Manager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'


class Book(TimeStampModel):
    name=models.CharField(max_length=254,null=False,blank=False)
    price=models.FloatField(default=0)
    author_name=models.CharField(max_length=254,null=True,blank=True)

    class Meta:
        db_table='book'