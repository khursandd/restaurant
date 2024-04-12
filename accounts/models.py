from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from accounts.managers import UserManager, CustomerManager, RestaurantManager


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        CUSTOMER = "CUSTOMER", 'Customer'
        RESTAURANT = "RESTAURANT", 'Restaurant'

    base_role = Role.ADMIN
    username = models.CharField(max_length=64, unique=True)
    role = models.CharField(max_length=64, choices=Role.choices, default=base_role)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Customer(User):
    base_role = User.Role.CUSTOMER
    customers = CustomerManager()

    def __str__(self):
        return self.base_role

    class Meta:
        proxy = True


class Restaurant(User):
    base_role = User.Role.RESTAURANT
    restaurants = RestaurantManager()

    def __str__(self):
        return self.base_role

    class Meta:
        proxy = True
