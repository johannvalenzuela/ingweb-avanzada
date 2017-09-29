from django.contrib import admin
from .models import *
# Register your models here.
entities = [
     Student,
     Teacher,
     Admin,
     Career,
     Programme,
     Enrolled,
     #Signature,
     #Instance_Signature,
     #Teacher_Signature,
     #Inscription,
     #Status_Inscription
    ]

admin.site.register(entities)