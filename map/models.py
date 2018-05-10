from django.db import models

# Create your models here.


class Shop(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    products = models.ManyToManyField('Product')


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    compound = models.TextField()
    price = models.FloatField()
    photo = models.URLField(null=True)
    energy = models.IntegerField()
    weight = models.FloatField()
    category = models.CharField(max_length=25)
