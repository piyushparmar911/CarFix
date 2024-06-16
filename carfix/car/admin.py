from django.contrib import admin
from .models import Car
# Register your models here.

    

class Caradmin(admin.ModelAdmin):
    list_display = ('name', 'carNo', 'model', 'color','image')
    
admin.site.register(Car,Caradmin)
    
