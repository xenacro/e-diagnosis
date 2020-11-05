from django.db import models


# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    mobile_number = models.CharField(max_length=10, unique=True)
    bio = models.TextField("Qualificatons: ", null=True, blank=True)

# Model for patient.

class Patient(models.Model):
    patientemail = models.EmailField("Enter Email", unique=True)
    docId = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=101)
    phone = models.CharField("Enter Without any country/state codes", max_length=10, unique=True)

    def __str__(self):
        return str(self.id)  # pylint: disable=no-member
# Model for Scans

class Scan(models.Model):
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    scans = models.FileField() #for storing scans
    result = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=1000)
    dateOfScan = models.DateField()

    def __str__(self):
        return str(self.id)  # pylint: disable=no-member
