from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# ESTUDIANTE
class Student(models.Model):
    rut_student = models.CharField(max_length=15)
    first_name_student = models.CharField(max_length=40)
    last_name_student = models.CharField(max_length=40)
    phone_student = models.IntegerField()
<<<<<<< HEAD
=======
    user = models.OneToOneField(User)
>>>>>>> 05b7afe2fd1d0b6e643016aee856b86e60eef1f4

@receiver(post_save, sender=User)
def create_user_student(sender, instance, created, **kwargs):
    if created:
        Student.object.create(user=instance)

@receiver(post_save, sender=User)
def save_user_student(sender, instance, **kwargs):
    instance.student.save()

# PROFESOR
class Teacher(models.Model):
    first_name_teacher = models.CharField(max_length=40)
    last_name_teacher = models.CharField(max_length=40)
    rut_teacher = models.CharField(max_length=15)
    phone_teacher = models.IntegerField()
<<<<<<< HEAD
=======
    user = models.OneToOneField(User)
>>>>>>> 05b7afe2fd1d0b6e643016aee856b86e60eef1f4

@receiver(post_save, sender=User)
def create_user_teacher(sender, instance, created, **kwargs):
    if created:
        Teacher.object.create(user=instance)

@receiver(post_save, sender=User)
def save_user_teacher(sender, instance, **kwargs):
    instance.teacher.save()

# ADMINISTRADOR
class Admin(models.Model):
    first_name_admin = models.CharField(max_length=40)
    last_name_admin = models.CharField(max_length=40)
    rut_admin = models.CharField(max_length=15)
    phone_admin = models.IntegerField()
<<<<<<< HEAD
=======
    user = models.OneToOneField(User)
>>>>>>> 05b7afe2fd1d0b6e643016aee856b86e60eef1f4

@receiver(post_save, sender=User)
def create_user_admin(sender, instance, created, **kwargs):
    if created:
        Admin.object.create(user=instance)

@receiver(post_save, sender=User)
def save_user_admin(sender, instance, **kwargs):
    instance.admin.save()

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
    name_program = models.CharField(max_length=40)
    description_program = models.CharField(max_length=40)
    state_program = models.CharField(max_length=20)
    period_program = models.CharField(max_length=15)

    def __str__(self):
        return self.name_program

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
    teacher = models.ManyToManyField(Teacher, through='List_Teacher')
    
    def __str__(self):
        return self.name_intance_signature

# MATRICULA
class Enrolled(models.Model):
    career = models.ForeignKey(Career)
    year = models.IntegerField()
    # Semestre
    period = models.IntegerField()
    student = models.ManyToManyField(Student,through='List_Student_Enrolled')
    instance_signature = models.ManyToManyField(Instance_Signature,through='List_Signature_Enrolled')
    name_enroll = models.CharField(max_length=40)
    description_enroll = models.CharField(max_length=40)
    state_enroll = models.CharField(max_length=40)

    def __str__(self):
        return self.name_enroll

# LISTA ESTUDIANTES MATRICULADOS
class List_Student_Enrolled(models.Model):
    idStudent = models.ForeignKey(Student)
    idEnrroled = models.ForeignKey(Enrolled)

    def __str__(self):
        return str(self.idStudent.rut_student)+" "+str(self.idEnrroled.name_enroll)

# LISTA ASIGNATURAS MATRICULA
class List_Signature_Enrolled(models.Model):
    idInstance_Signature = models.ForeignKey(Instance_Signature)
    idEnrroled = models.ForeignKey(Enrolled)

    def __str__(self):
        return str(self.idInstance_Signature.name_instance_signature)+" "+str(self.idEnrroled.name_enroll)

# LISTA ASIGNATURAS
class List_Teacher(models.Model):
    idInstance_Signature = models.ForeignKey(Instance_Signature)
    idTeacher = models.ForeignKey(Teacher)

    def __str__(self):
        return str(self.idTeacher.name_teacher)+" "+str(self.idInstance_Signature.name_instance_signature)

# INSCRIPCION ASIGNATURA
class Inscription(models.Model):
    intance_signature = models.ManyToManyField(Instance_Signature, through='List_Inscription_Instance_Signature')
    student = models.ManyToManyField(Student, through='List_Student')
    name_inscription = models.CharField(max_length=40)
    description_inscription = models.CharField(max_length=40)

    def __str__(self):
        return self.name_inscription

# LISTA INSCRIPCION ASIGNATURA
class List_Inscription_Instance_Signature(models.Model):
    idInstance_Signature = models.ForeignKey(Instance_Signature)
    idInscription = models.ForeignKey(Inscription)

    def __str__(self):
        return str(self.idInscription.name_inscription)+" "+str(self.idInstance_Signature.name_instance_signature)

class List_Student(models.Model):
    idStudent = models.ForeignKey(Student)
    idInscription = models.ForeignKey(Inscription)

    def __str__(self):
        return str(self.idInscription.name_inscription)+" "+str(self.idStudent.rut_student)

# ESTADO INSCRIPCION
class Status_Inscription(models.Model):
    name_status = models.CharField(max_length=20)
    end_status = models.CharField(max_length=20)
    inscription = models.ForeignKey(Inscription)

    def __str__(self):
        return self.name_status

