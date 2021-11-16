from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
from Resources_Module.models import Hospital

# Create your models here


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique = True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    is_normal_user = models.BooleanField(default=True)
    is_hospital_staff = models.BooleanField(default=False,verbose_name="Tick the checkbox if you are a hospital employee")
    hospital = models.OneToOneField(Hospital, on_delete=CASCADE, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
      return "{}".format(self.email)


class HospitalStaff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=CASCADE)

    def __str__(self):
      return "{}".format(self.user.email)