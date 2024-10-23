from django.db import models

# Create your models here.

class Product(models.Model):
    camera = models.CharField(max_length=200)
    display = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    link = models.TextField()
    processor = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)
    ratings = models.CharField(max_length=200)
    star = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    warranty = models.CharField(max_length=200)
    battery = models.CharField(max_length=200)