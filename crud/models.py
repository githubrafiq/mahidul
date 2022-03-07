from django.db import models
from django.utils import timezone

# Create your models here.

class Education(models.Model):
    level = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)

    def __str__(self):
        return self.institute

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    subjects = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)

    def __str__(self):
        return self.job_title


class Details(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    