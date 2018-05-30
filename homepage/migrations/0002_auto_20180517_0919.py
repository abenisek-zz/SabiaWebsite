# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-17 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneNumber', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SessionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubjectName', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('Age', models.IntegerField()),
                ('AddressID', models.CharField(max_length=200)),
                ('LocationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Location')),
                ('PhoneID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Phone')),
            ],
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserType', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='userlogin',
            name='UserTypeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.UserType'),
        ),
        migrations.AddField(
            model_name='scheduledsession',
            name='SubjectID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Subjects'),
        ),
        migrations.AddField(
            model_name='phone',
            name='PhoneTypeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.PhoneType'),
        ),
    ]
