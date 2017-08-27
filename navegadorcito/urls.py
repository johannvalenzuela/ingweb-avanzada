from django.conf.urls import *
from django.contrib import admin
from navegadorcito.views import index, login_admin, login_student, login_teacher, courses_teacher, dashboard_teacher

urlpatterns = [
    url(r'^$', index),
    url(r'^student/', login_student),
    url(r'^teacher/dashboard', dashboard_teacher),
    url(r'^teacher/courses', courses_teacher),
    url(r'^teacher/', login_teacher),
    
    url(r'^admin/', login_admin),
]
