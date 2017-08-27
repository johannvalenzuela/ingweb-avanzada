from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def login_admin(request):
    return render(request, 'admin/login.html', {})

def login_teacher(request):
    return render(request, 'teacher/login.html', {})

def login_student(request):
    return render(request, 'student/login.html', {})

def dashboard_student(request):
    return render(request, 'student/dashboard.html', {})

def dashboard_teacher(request):
    return render(request, 'teacher/dashboard.html', {})

def dashboard_admin(request):
    return render(request, 'admin/dashboard.html', {})

def courses_teacher(request):
    return render(request, 'teacher/courses.html', {})

def courses_student(request):
    return render(request, 'student/courses.html', {})

def profile_student(request):
    return render(request, 'student/profile.html', {})

