from django.db import models
from datetime import datetime

# Create your models here.
class Employer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    date = models.CharField(max_length=30)
    pay = models.CharField(max_length=100)




class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    experience = models.CharField(max_length=5000)
    date = models.CharField(max_length=30)
    salary = models.CharField(max_length=100)
