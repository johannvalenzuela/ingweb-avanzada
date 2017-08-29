from django.contrib import admin
from .models import *
# Register your models here.
entities = [
     Student,
     Teacher,
     Admin,
     Career,
     Programme,
     Signature,
     Instance_Signature,
     Enrolled,
     List_Student_Enrolled,
     List_Signature_Enrolled,
     List_Teacher,
     Inscription,
     List_Inscription_Instance_Signature,
     List_Student,
     Status_Inscription]

admin.site.register(entities)