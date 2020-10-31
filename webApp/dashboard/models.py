from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    mobile_number = models.CharField(max_length=10, unique=True)
    bio = models.TextField("Qualificatons: ", null=True, blank=True)

# Model for patient.

class patientForm(models.Model):
    patientemail = models.EmailField("Enter Email", unique=True)
    docId = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=101)
    phone = models.CharField("Enter Without any country/state codes", max_length=10, unique=True)
    class Meta:
        db_table = "patient"

# Model for Scans

class scansForm(models.Model):
    patientId = models.ForeignKey(patientForm, on_delete=models.CASCADE)
    scans = models.FileField() #for storing scans
    result = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=1000)
    dateOfScan = models.DateField()
    class Meta:
        db_table = "scans"
