from django.db import models

# Create your models here.

class Product(models.Model):
    pid = models.CharField(max_length=100,blank=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    star = models.CharField(max_length=200)
    
    ratings = models.CharField(max_length=200)
    link = models.TextField()

    details = models.JSONField(default=dict)
