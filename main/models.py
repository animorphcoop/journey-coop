from django.apps import apps
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.core.validators import FileExtensionValidator
from django_countries.fields import CountryField


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    username = None
    first_name = None
    last_name = None
    nickname = models.CharField(
        verbose_name=_("Nickname"),
        max_length=30,
        help_text=_("Will be shown alongside entries"),
        null=True,
    )
    country = CountryField(null=True,)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self) -> str:
        if self.nickname:
            return self.nickname
        else:
            return self.email


class Journey(models.Model):
    ALLOWED_AUDIO_TYPES = ['wav', 'wma', 'mp3', 'aiff', 'aac', 'm4a']
    ALLOWED_IMAGE_TYPES = ['jpg', 'jpeg', 'gif', 'svg', 'webp', 'png']

    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=80)
    summary = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/', blank=True,
                              validators=[FileExtensionValidator(ALLOWED_IMAGE_TYPES)],
                              )
    audio = models.FileField(upload_to='audio/',
                             blank=True,
                             validators=[FileExtensionValidator(ALLOWED_AUDIO_TYPES)],
                             )
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Response(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=500)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
