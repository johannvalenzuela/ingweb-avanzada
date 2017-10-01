from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from navegadorcito.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^student/dashboard', dashboard_student),
    url(r'^students/(?P<idStudent>[0-9]+)/courses$', courses_student, name='courses_student' ),
    url(r'^students/(?P<idStudent>[0-9]+)$',student,name='student'),
    url(r'^student/profile', student),
    url(r'^admin/dashboard', dashboard_admin),
 #   url(r'^admin/', login_admin),
    url(r'^teacher/dashboard', dashboard_teacher),
    url(r'^teacher/courses', courses_teacher),
    url(r'^teacher/asignature/(?P<pk>[0-9]+)/$', asignature_detail, name='asignature_detail'),
    url(r'^teacher/', login_teacher),
    
    
   # url(r'^admin/', login_admin),
]
