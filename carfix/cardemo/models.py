from django.db import models

# Create your models here.

   
class Role(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class webUser(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, unique=True, null=True)
    password = models.CharField(max_length=200, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
          return self.name

class Car(models.Model):
    name = models.CharField(max_length=200, null=True)
    model = models.CharField(max_length=200, null=True)
    carNo = models.CharField(max_length=200, unique=True, null=True)
    color = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    
    def __str__(self):
        return self.name
    
class Slot(models.Model):
    time = models.TimeField(max_length=200, null=True)
    date = models.DateField(max_length=200, null=True)
    
    def __str__(self):
        return f"{self.date} at {self.time}"

class CarSlot(models.Model):
    carId = models.ForeignKey(Car, on_delete=models.CASCADE)
    slotId = models.ForeignKey(Slot, on_delete=models.CASCADE)
    userId = models.ForeignKey(webUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.carId} booked by {self.userId} on {self.slotId}"