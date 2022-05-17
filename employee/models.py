from django.db import models
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='/media/resume')

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    staff_id = models.CharField(max_length=255, null=True, blank=True, unique=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    resume = models.FileField(default="")

    def __str__(self):
        return self.first_name