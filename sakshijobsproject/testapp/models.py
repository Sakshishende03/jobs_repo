from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField(default='example@example.com')  # Set your default email value here
    phonenumber = models.BigIntegerField()

class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField(default='example@example.com')  # Set your default email value here
    phonenumber = models.BigIntegerField()

class BangJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField(default='example@example.com')  # Set your default email value here
    phonenumber = models.BigIntegerField()

