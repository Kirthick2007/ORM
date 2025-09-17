from django.contrib import admin
from . models import Car
admin.site.register = (Car)

class CarAdmin(admin.ModelAdmin): 
    list_display=('Car_ID', 'Car_name', 'Release_date', 'Brand', 'Company','type' )