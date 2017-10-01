# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-30 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navegadorcito', '0002_auto_20170929_1935'),
    ]

    operations = [
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
                ('inscriptions', models.ManyToManyField(through='navegadorcito.Inscription', to='navegadorcito.Student')),
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
            name='Teacher_Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idInstance_Signature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Instance_Signature')),
                ('idTeacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='instance_signature',
            name='list_teacher',
            field=models.ManyToManyField(through='navegadorcito.Teacher_Signature', to='navegadorcito.Teacher'),
        ),
        migrations.AddField(
            model_name='instance_signature',
            name='signature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Signature'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='idInstance_Signature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Instance_Signature'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='idStudent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navegadorcito.Student'),
        ),
    ]
