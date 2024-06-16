from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=200, null=True)
    model = models.CharField(max_length=200, null=True)
    carNo = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images/', null=True)