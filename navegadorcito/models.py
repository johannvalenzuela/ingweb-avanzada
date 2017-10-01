from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# ESTUDIANTE
class Student(models.Model):
    rut_student = models.CharField(max_length=15)
    first_name_student = models.CharField(max_length=40)
    last_name_student = models.CharField(max_length=40)
    phone_student = models.CharField(max_length=15)
    email_student = models.CharField(max_length=30)
    address_student = models.CharField(max_length=30)
    password_student = models.CharField(max_length=20)  

    def __str__(self):
        return self.rut_student

# PROFESOR
class Teacher(models.Model):
    first_name_teacher = models.CharField(max_length=40)
    last_name_teacher = models.CharField(max_length=40)
    rut_teacher = models.CharField(max_length=15)
    phone_teacher = models.CharField(max_length=15)
    email_teacher = models.CharField(max_length=30)
    address_teacher = models.CharField(max_length=30)
    password_teacher = models.CharField(max_length=20)

    def __str__(self):
        return self.rut_teacher

# ADMINISTRADOR
class Admin(models.Model):
    first_name_admin = models.CharField(max_length=40)
    last_name_admin = models.CharField(max_length=40)
    rut_admin = models.CharField(max_length=15)
    phone_admin = models.CharField(max_length=15)
    address_admin = models.CharField(max_length=30)
    password_admin = models.CharField(max_length=20)
    email_admin = models.CharField(max_length=30)

    def __str__(self):
        return self.rut_admin

# CARRERA
class Career(models.Model):
    name_career = models.CharField(max_length=40)
    description_career = models.CharField(max_length=40)
    acronym_career = models.CharField(max_length=4)
    state_career = models.CharField(max_length=20)

    def __str__(self):
        return self.name_career

# MALLA
class Programme(models.Model):
    career = models.ForeignKey(Career)
    enrolleds = models.ManyToManyField(Student,through='Enrolled')
    name_program = models.CharField(max_length=40)
    description_program = models.CharField(max_length=40)
    state_program = models.CharField(max_length=20)
    period_program = models.CharField(max_length=15)

    def __str__(self):
        return self.name_program

# MATRICULA
class Enrolled(models.Model):
    idStudent = models.ForeignKey(Student, null=True)
    idProgramme = models.ForeignKey(Programme, null=True)
    year = models.IntegerField()
    period = models.IntegerField()

    def __str__(self):
        return str(self.idStudent)+" "+str(self.idProgramme)

# ASIGNATURA
class Signature(models.Model):
    key_signature = models.CharField(max_length=8)
    program = models.ForeignKey(Programme)
    name_signature = models.CharField(max_length=40)
    description_signature = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name_signature
    


#INSTANCIA ASIGNATURA
class Instance_Signature(models.Model):
    signature = models.ForeignKey(Signature)
    year = models.IntegerField()
    parallel = models.IntegerField()
    semester = models.IntegerField()
    name_instance_signature = models.CharField(max_length=40)
    slot_signature = models.IntegerField()
    list_teacher = models.ManyToManyField(Teacher, through='Teacher_Signature')
    inscriptions = models.ManyToManyField(Student, through='Inscription')
    
    def __str__(self):
        return self.name_instance_signature

#LISTA ASIGNATURAS PROFESOR
class Teacher_Signature(models.Model):
    idTeacher = models.ForeignKey(Teacher, null=True)
    idInstance_Signature = models.ForeignKey(Instance_Signature, null=True)

    def __str__(self):
       return str(self.idTeacher)+" "+str(self.idInstance_Signature)
   

# INSCRIPCION ASIGNATURA
class Inscription(models.Model):
    idStudent = models.ForeignKey(Student)
    idInstance_Signature = models.ForeignKey(Instance_Signature)
    name_inscription = models.CharField(max_length=40)
    description_inscription = models.CharField(max_length=40)

    def __str__(self):
       return str(self.idStudent)+" "+str(self.idInstance_Signature)

# ESTADO INSCRIPCION
class Status_Inscription(models.Model):
    name_status = models.CharField(max_length=20)
    end_status = models.CharField(max_length=20)
    inscription = models.ForeignKey(Inscription)

    def __str__(self):
        return self.name_status

