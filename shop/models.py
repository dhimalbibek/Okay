from django.db import models

# Create your models here.
class category(models.Model):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.CharField(max_length=200)


