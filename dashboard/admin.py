from django.contrib import admin
from .models import Soldier, Machine, License

# Register your models here.

class SoldierAdmin(admin.ModelAdmin):
    fields = ['name', 'email']

admin.site.register(Soldier, SoldierAdmin)

class MachineAdmin(admin.ModelAdmin):
    fields = ['serial_number', 'assigned_to']
admin.site.register(Machine, MachineAdmin)

class LicenseAdmin(admin.ModelAdmin):
    fields = ['name', 'key', 'pub_date', 'start_date', 'end_date', 'licenses_remaining', 'on_machine']
admin.site.register(License,LicenseAdmin)

