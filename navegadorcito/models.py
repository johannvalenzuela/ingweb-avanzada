from django.db import models

# Create your models here.
class Students(models.Model):
    id_student = models.AutoField(primary_key=True)
    first_name_student = models.CharField(max_length=40, default="No data")
    last_name_student = models.CharField(max_length=40, default="No data")
    rut_student = models.CharField(max_length=15)
    mail_student = models.CharField(max_length=90)


class Teachers(models.Model):
    id_teacher = models.AutoField(primary_key=True)
    first_name_teacher = models.CharField(max_length=40, default="No data")
    last_name_teacher = models.CharField(max_length=40, default="No data")
    rut_teacher = models.CharField(max_length=15)
    mail_teacher = models.CharField(max_length=90)

class Admins(models.Model):
    id_admin = models.AutoField(primary_key=True)
    first_name_admin = models.CharField(max_length=40, default="No data")
    last_name_admin = models.CharField(max_length=40, default="No data")
    rut_admin = models.CharField(max_length=15)
    mail_admin = models.CharField(max_length=90)

class Careers(models.Model):
    id_career = models.AutoField(primary_key=True)
    name_career = models.CharField(max_length=40)
    description_career = models.CharField(max_length=40, default="")

class Programmes(models.Model):
    id_program = models.AutoField(primary_key=True)
    career = models.ForeignKey(Careers)
    name_program = models.CharField(max_length=40)
    description_program = models.CharField(max_length=40, default="")

class Signatures(models.Model):
    id_signature = models.AutoField(primary_key=True)
    acronym = models.CharField(max_length=3)
    program = models.ForeignKey(Programmes)
    teacher = models.ManyToManyField(Teachers)
    name_signature = models.CharField(max_length=40)
    description_signature = models.CharField(max_length=40, default="")

# Matrícula
class Enrolleds(models.Model):
    id_enroll = models.AutoField(primary_key=True)
    career = models.ForeignKey(Careers)
    state = models.CharField(max_length=15)
    year = models.IntegerField()
    # Semestre
    period = models.IntegerField()
    student = models.ManyToManyField(Students)
    name_enroll = models.CharField(max_length=40)
    description_enroll = models.CharField(max_length=40, default="")
    state_enroll = models.CharField(max_length=40, default="")

# Inscripción a las asignaturas
class Inscription(models.Model):
    id_inscription = models.AutoField(primary_key=True)
    signature = models.ManyToManyField(Signatures)
    student = models.ManyToManyField(Students)
    name_inscription = models.CharField(max_length=40)
    description_inscription = models.CharField(max_length=40, default="")