from django.db import models

# Create your models here.

class App (models.Model):
    firstName = models.CharField (max_length=100)
    lastName = models.CharField (max_length=100)
    email = models.CharField (max_length=50)
    phoneNumber = models.CharField (max_length=20)
    age = models.CharField (max_length=20)
