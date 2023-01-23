from django.db import models

# Create your models here.

class About(models.Model):
    name =models.CharField(max_length=50)
    address =models.CharField(max_length=50)
    price =models.IntegerField()
    image =models.ImageField()