

from django.db import models
from django.utils import timezone


# Create your models here.

class OldStudents(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    address = models.TextField()
    post = models.CharField(max_length=100)
    pin = models.IntegerField(default=0000)
    phone = models.CharField(max_length=10)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    whatsapp = models.CharField(max_length=10)
    email = models.EmailField()
    date_admission = models.DateField()
    date_left = models.DateField()
    qualification = models.CharField(max_length=100)
    is_qualification = models.CharField(max_length=100)
    member_id = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    division = models.CharField(max_length=50)
    place_holding = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
