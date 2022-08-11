from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.contrib.auth.models import (
  BaseUserManager,
  AbstractBaseUser,
  PermissionsMixin,
)


class CustomUserManager(BaseUserManager):

    def create_user(self, email, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, username and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,

            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        """
        Creates and saves a Super User with the given email, username and password.
        """

        extra_fields.setdefault('role', 1)
        if extra_fields.get('role') != 1:
            raise ValueError('Superuser must have role of Global Admin')

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            **extra_fields,
        )

        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    username = models.CharField(
        verbose_name='username',
        max_length=255,
        null=True,
    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_regex = RegexValidator(regex=r"(^(\+8801|8801|01|008801))[1|3-9]{1}(\d){8}$",
                                 message="Phone number must be entered in the format: '+8801865632882'. "
                                         "Up to 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex, MaxLengthValidator(13), MinLengthValidator(13)], max_length=13, blank=True, unique=True)

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, blank=True, null=True)

    date_of_birth = models.CharField(max_length=255, blank=True, null=True)

    ADMIN = 1
    Customer = 2

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (Customer, 'Customer'),

    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    joining_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'role']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


