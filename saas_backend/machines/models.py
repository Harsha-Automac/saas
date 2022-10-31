from django.db import models

# Create your models here.


class Machine_details(models.Model):
    objects = models.Manager()
    machine_id = models.CharField(max_length=120)
    machine_name = models.CharField(max_length=120)
    machine_model = models.CharField(max_length=120)
    machine_location = models.CharField(max_length=120)
    machine_doi = models.CharField(max_length=120)
    factory_id = models.CharField(max_length=120)
    
    @property
    def detail1(self):
        return self.machine_location,self.machine_doi


class Machine_tech_details(models.Model):
    objects = models.Manager()
    machine_id = models.CharField(max_length=120)
    component_name = models.CharField(max_length=120)
    warenty_status = models.CharField(max_length=120)
