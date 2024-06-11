from django.contrib import admin
from .models import Car
# Register your models here.

    

class Caradmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'image')
    
admin.site.register(Car,Caradmin)
    
