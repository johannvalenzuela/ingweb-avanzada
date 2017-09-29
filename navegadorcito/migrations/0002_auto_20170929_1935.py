# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 22:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navegadorcito', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='intance_signature',
        ),
        migrations.RemoveField(
            model_name='inscription',
            name='student',
        ),
        migrations.RemoveField(
            model_name='instance_signature',
            name='signature',
        ),
        migrations.RemoveField(
            model_name='instance_signature',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='list_inscription_instance_signature',
            name='idInscription',
        ),
        migrations.RemoveField(
            model_name='list_inscription_instance_signature',
            name='idInstance_Signature',
        ),
        migrations.RemoveField(
            model_name='list_signature_enrolled',
            name='idEnrroled',
        ),
        migrations.RemoveField(
            model_name='list_signature_enrolled',
            name='idInstance_Signature',
        ),
        migrations.RemoveField(
            model_name='list_student',
            name='idInscription',
        ),
        migrations.RemoveField(
            model_name='list_student',
            name='idStudent',
        ),
        migrations.RemoveField(
            model_name='list_student_enrolled',
            name='idEnrroled',
        ),
        migrations.RemoveField(
            model_name='list_student_enrolled',
            name='idStudent',
        ),
        migrations.RemoveField(
            model_name='list_teacher',
            name='idInstance_Signature',
        ),
        migrations.RemoveField(
            model_name='list_teacher',
            name='idTeacher',
        ),
        migrations.RemoveField(
            model_name='signature',
            name='program',
        ),
        migrations.RemoveField(
            model_name='status_inscription',
            name='inscription',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='birth_date_admin',
        ),
        migrations.RemoveField(
            model_name='enrolled',
            name='career',
        ),
        migrations.RemoveField(
            model_name='enrolled',
            name='description_enroll',
        ),
        migrations.RemoveField(
            model_name='enrolled',
            name='instance_signature',
        ),
        migrations.RemoveField(
            model_name='enrolled',
            name='name_enroll',
        ),
        migrations.RemoveField(
            model_name='enrolled',
            name='state_enroll',
        ),
        migrations.RemoveField(
            model_name='enrolled',
            name='student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='birth_date_student',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='birth_date_teacher',
        ),
        migrations.AddField(
            model_name='enrolled',
            name='idProgramme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Programme'),
        ),
        migrations.AddField(
            model_name='enrolled',
            name='idStudent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Student'),
        ),
        migrations.AddField(
            model_name='programme',
            name='enrolleds',
            field=models.ManyToManyField(through='navegadorcito.Enrolled', to='navegadorcito.Student'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='phone_admin',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_teacher',
            field=models.CharField(max_length=15),
        ),
        migrations.DeleteModel(
            name='Inscription',
        ),
        migrations.DeleteModel(
            name='Instance_Signature',
        ),
        migrations.DeleteModel(
            name='List_Inscription_Instance_Signature',
        ),
        migrations.DeleteModel(
            name='List_Signature_Enrolled',
        ),
        migrations.DeleteModel(
            name='List_Student',
        ),
        migrations.DeleteModel(
            name='List_Student_Enrolled',
        ),
        migrations.DeleteModel(
            name='List_Teacher',
        ),
        migrations.DeleteModel(
            name='Signature',
        ),
        migrations.DeleteModel(
            name='Status_Inscription',
        ),
    ]