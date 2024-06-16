from django.contrib import admin
from .models import User,Car,Role,Slot,CarSlot
# Register your models here.

    
class Useradmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'role')

class Caradmin(admin.ModelAdmin):
    list_display = ('name', 'carNo', 'model', 'color','image')
    
    
class Roleadmin(admin.ModelAdmin):
    list_display = ('name',)
    
class Slotadmin(admin.ModelAdmin):
    list_display = ('time','date')
    
class CarSlotadmin(admin.ModelAdmin):
    list_display = ('carId','slotId','userId')
    
admin.site.register(User,Useradmin)
admin.site.register(Car,Caradmin)
admin.site.register(Role,Roleadmin)
admin.site.register(Slot,Slotadmin)
admin.site.register(CarSlot,CarSlotadmin)
    
