from django.db import models

# Create your models here.

class Machine_details(models.Model):
    machine_id = models.CharField(max_length=120)
    machine_name = models.CharField(max_length=120)
    machine_model = models.CharField(max_length=120)
    machine_location = models.CharField(max_length=120)
    machine_doi = models.CharField(max_length=120)
    factory_id = models.CharField(max_length=120)
