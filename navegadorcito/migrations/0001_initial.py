# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_admin', models.CharField(max_length=40)),
                ('last_name_admin', models.CharField(max_length=40)),
                ('rut_admin', models.CharField(max_length=15)),
                ('phone_admin', models.IntegerField()),
                ('birth_date_admin', models.DateField()),
                ('address_admin', models.CharField(max_length=30)),
                ('password_admin', models.CharField(max_length=20)),
                ('email_admin', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_career', models.CharField(max_length=40)),
                ('description_career', models.CharField(max_length=40)),
                ('acronym_career', models.CharField(max_length=4)),
                ('state_career', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Enrolled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('period', models.IntegerField()),
                ('name_enroll', models.CharField(max_length=40)),
                ('description_enroll', models.CharField(max_length=40)),
                ('state_enroll', models.CharField(max_length=40)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Career')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_inscription', models.CharField(max_length=40)),
                ('description_inscription', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Instance_Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('parallel', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('name_instance_signature', models.CharField(max_length=40)),
                ('slot_signature', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='List_Inscription_Instance_Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idInscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Inscription')),
                ('idInstance_Signature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Instance_Signature')),
            ],
        ),
        migrations.CreateModel(
            name='List_Signature_Enrolled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEnrroled', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Enrolled')),
                ('idInstance_Signature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Instance_Signature')),
            ],
        ),
        migrations.CreateModel(
            name='List_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idInscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Inscription')),
            ],
        ),
        migrations.CreateModel(
            name='List_Student_Enrolled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEnrroled', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Enrolled')),
            ],
        ),
        migrations.CreateModel(
            name='List_Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idInstance_Signature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Instance_Signature')),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_program', models.CharField(max_length=40)),
                ('description_program', models.CharField(max_length=40)),
                ('state_program', models.CharField(max_length=20)),
                ('period_program', models.CharField(max_length=15)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Career')),
            ],
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_signature', models.CharField(max_length=8)),
                ('name_signature', models.CharField(max_length=40)),
                ('description_signature', models.CharField(max_length=40)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Programme')),
            ],
        ),
        migrations.CreateModel(
            name='Status_Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_status', models.CharField(max_length=20)),
                ('end_status', models.CharField(max_length=20)),
                ('inscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Inscription')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_student', models.CharField(max_length=15)),
                ('first_name_student', models.CharField(max_length=40)),
                ('last_name_student', models.CharField(max_length=40)),
                ('phone_student', models.CharField(max_length=15)),
                ('email_student', models.CharField(max_length=30)),
                ('birth_date_student', models.DateField()),
                ('address_student', models.CharField(max_length=30)),
                ('password_student', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_teacher', models.CharField(max_length=40)),
                ('last_name_teacher', models.CharField(max_length=40)),
                ('rut_teacher', models.CharField(max_length=15)),
                ('phone_teacher', models.IntegerField()),
                ('email_teacher', models.CharField(max_length=30)),
                ('birth_date_teacher', models.DateField()),
                ('address_teacher', models.CharField(max_length=30)),
                ('password_teacher', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='list_teacher',
            name='idTeacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Teacher'),
        ),
        migrations.AddField(
            model_name='list_student_enrolled',
            name='idStudent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Student'),
        ),
        migrations.AddField(
            model_name='list_student',
            name='idStudent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Student'),
        ),
        migrations.AddField(
            model_name='instance_signature',
            name='signature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Signature'),
        ),
        migrations.AddField(
            model_name='instance_signature',
            name='teacher',
            field=models.ManyToManyField(through='navegadorcito.List_Teacher', to='navegadorcito.Teacher'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='intance_signature',
            field=models.ManyToManyField(through='navegadorcito.List_Inscription_Instance_Signature', to='navegadorcito.Instance_Signature'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='student',
            field=models.ManyToManyField(through='navegadorcito.List_Student', to='navegadorcito.Student'),
        ),
        migrations.AddField(
            model_name='enrolled',
            name='instance_signature',
            field=models.ManyToManyField(through='navegadorcito.List_Signature_Enrolled', to='navegadorcito.Instance_Signature'),
        ),
        migrations.AddField(
            model_name='enrolled',
            name='student',
            field=models.ManyToManyField(through='navegadorcito.List_Student_Enrolled', to='navegadorcito.Student'),
        ),
    ]
