from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    image_url = models.URLField(max_length=255, blank=True, null=True)

class Department(models.Model):
    name = models.CharField(max_length=255)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

class City(models.Model):
    name = models.CharField(max_length=255)
