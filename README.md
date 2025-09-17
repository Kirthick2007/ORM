# Ex02 Django ORM Web Application


## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
from django.db import models

class Car(models.Model):
    Car_ID = models.IntegerField(primary_key=True) 
    Car_name = models.CharField(max_length=100) 
    Release_date=models.DateField()
    Brand=models.CharField(max_length=50) 
    Company=models.CharField(max_length=100)
    type = models.CharField(max_length=50)

class CarAdmin(admin.ModelAdmin): 
    list_display=('Car_ID', 'Car_name', 'Release_date', 'Brand', 'Company','type' )
```



## OUTPUT

Include the screenshot of your admin page.


## RESULT
Thus the program for creating a database using ORM hass been executed successfully


