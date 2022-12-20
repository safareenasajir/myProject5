from django.db import models

# Create your models here.
class Bank(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=50)
    cpassword= models.CharField(max_length=50)
    def __str__(self):
        return self.username
