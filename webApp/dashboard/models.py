from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    mobile_number = models.CharField(max_length=10, unique=True)
    bio = models.TextField(null=True, blank=True)
