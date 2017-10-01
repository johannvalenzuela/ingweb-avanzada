from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Programme,Enrolled,Inscription
from django.core import serializers
# Create your views here.

def index(request):

    return render(request, 'index.html', {})

#def login_admin(request):
#    return render(request, 'admin/login.html', {})

def login_teacher(request):
    return render(request, 'teacher/login.html', {})

def login_student(request):
    return render(request, 'student/login.html', {})

def dashboard_student(request,idStudent):
    return render(request, 'student/dashboard.html', {})

def dashboard_teacher(request):
    return render(request, 'teacher/dashboard.html', {})

def dashboard_admin(request):
    return render(request, 'admin/dashboard.html', {}) 

def courses_teacher(request):
    return render(request, 'teacher/courses.html', {})

def courses_student(request,idStudent):
    instance_signature_list=Inscription.objects.all().filter(idStudent=idStudent).instance_signature
   # matriculas=students.Programme.all()
 #   print(students.Enrolled.all())
    return render(request,'student/courses.html', {"signature_list": instance_signature_list})

def student(request,idStudent):
    student=Student.objects.get(pk=idStudent)
   # matriculas=students.Programme.all()
 #   print(students.Enrolled.all())
    print(student)
    return render(request,'student/profile.html', {"student": student})

def profile_student(request,idStudent):
    student=Student.objects.get(pk=idStudent)
   # matriculas=students.Programme.all()
 #   print(students.Enrolled.all())
    print(student)
    return render(request,'student/profile.html', {"student": student})
"""
def equipo(request,idEquipo):
    equipo=Equipo.objects.get(pk=idEquipo)
    incidencias=equipo.Incidencias.all()
    #print(equipo.Lista_Incidencia.all())
    #print (equipo.Incidencias.filter(idEquipo__idincidencias=idIncidencia))
    #Incidencia.objects.filter()
    #incidencias=Lista_Incidencia.objects.all().filter(idEquipo__id=idEquipo)
    atributos=Lista_Atributo.objects.all().filter(idEquipo__id=idEquipo)
    print(incidencias)
    listaincidencia=IncidenciaTable(incidencias)
    #print(atributos)
    return render(request,'inventario/equipo.html',{"equipo": equipo, "atributos":atributos, "listaincidencia":listaincidencia})
"""

def asignature_detail(request, pk):

    return render(request, 'teacher/asignature.html', {})