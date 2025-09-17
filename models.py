from django.db import models

class Car(models.Model):
    Car_ID = models.IntegerField(primary_key=True) 
    Car_name = models.CharField(max_length=100) 
    Release_date=models.DateField()
    Brand=models.CharField(max_length=50) 
    Company=models.CharField(max_length=100)
    type = models.CharField(max_length=50)

