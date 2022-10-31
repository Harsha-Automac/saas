from django.contrib import admin

# Register your models here.
from .models import Machine_details,Machine_tech_details

admin.site.register(Machine_details)
admin.site.register(Machine_tech_details)
