import os

from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.

def custom_upload_to(instance, filename):
    # Extract the file extension
    ext = filename.split('.')[-1]

    # Generate the filename using the student's name and primary key
    # Slugify the name to ensure it's URL-safe
    # Include the primary key to avoid conflicts
    filename = f"{slugify(instance.name)}-{instance.pk}.{ext}"

    # Return the full path to the file
    return os.path.join('images', filename)


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
    image = models.FileField(upload_to=custom_upload_to, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
