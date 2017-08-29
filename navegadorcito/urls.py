from django.conf.urls import *
from django.contrib import admin
from navegadorcito.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^student/dashboard', dashboard_student),
    url(r'^student/courses', courses_student),
    url(r'^student/', login_student),
    url(r'^admin/dashboard', dashboard_admin),
    url(r'^admin/', login_admin),
    url(r'^teacher/dashboard', dashboard_teacher),
    url(r'^teacher/courses', courses_teacher),
    url(r'^teacher/', login_teacher),
    
   # url(r'^admin/', login_admin),
]
