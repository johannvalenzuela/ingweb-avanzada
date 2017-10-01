from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Programme,Enrolled,Inscription,Instance_Signature,Signature,Teacher,Status_Inscription
from django.core import serializers
# Create your views here.

def index(request):

    return render(request, 'index.html', {})

def login_teacher(request):
    return render(request, 'teacher/login.html', {})

def login_student(request):
    return render(request, 'student/login.html', {})

def dashboard_student(request,idStudent):
    student=Student.objects.get(pk=idStudent)
    actual_signature_list=Status_Inscription.objects.all().filter(name_status="Válida",inscription__idStudent=idStudent)
    print(actual_signature_list)
    return render(request, 'student/dashboard.html', {"student": student, "signature_list": actual_signature_list})

def dashboard_teacher(request,idTeacher):
    teacher=Teacher.objects.get(pk=idTeacher)
    actual_signature_list=Status_Inscription.objects.all().filter(name_status="Válida",inscription__idInstance_Signature__list_teacher=idTeacher)
    print(actual_signature_list)
    return render(request, 'teacher/dashboard.html', {"teacher": teacher, "signature_list": actual_signature_list})

def dashboard_admin(request):
    return render(request, 'admin/dashboard.html', {}) 

def courses_teacher(request):
    return render(request, 'teacher/courses.html', {})

def courses_student(request,idStudent):
    student=Student.objects.get(pk=idStudent)     
    instance_signature_list=Instance_Signature.objects.all().filter(inscriptions=idStudent)

    print(instance_signature_list)
    return render(request,'student/courses.html', {"signature_list": instance_signature_list})

def courses_teacher(request,idTeacher):
    teacher=Teacher.objects.get(pk=idTeacher)     
    instance_signature_list=Instance_Signature.objects.all().filter(list_teacher=idTeacher)
    print(instance_signature_list)
    return render(request,'teacher/courses.html', {"signature_list": instance_signature_list})

def student(request,idStudent):
    student=Student.objects.get(pk=idStudent)
    print(student)
    return render(request,'student/profile.html', {"student": student})

def profile_student(request,idStudent):
    student=Student.objects.get(pk=idStudent)
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

def signature_detail(request,idSignature):
    signature=Signature.objects.get(pk=idSignature)
    print(signature)
    return render(request,'signature.html', {"signature": signature})