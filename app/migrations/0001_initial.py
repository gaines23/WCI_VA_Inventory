# Generated by Django 3.0.9 on 2021-06-03 21:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignempgarm',
            fields=[
                ('garmentid', models.AutoField(db_column='GarmentID', primary_key=True, serialize=False)),
                ('dateassigned', models.DateField(blank=True, db_column='DateAssigned', default=datetime.date.today, null=True)),
                ('quantity', models.IntegerField(blank=True, db_column='Quantity', default=' ', null=True)),
                ('replacement', models.CharField(blank=True, choices=[(0, 'No'), (1, 'Yes')], db_column='Replacement', max_length=10, null=True)),
                ('garmtype', models.CharField(blank=True, db_column='GarmType', default=' ', max_length=255, null=True)),
                ('garmsize', models.CharField(blank=True, db_column='GarmSize', default=' ', max_length=20, null=True)),
            ],
            options={
                'db_table': 'AssignEmpGarm',
                'ordering': ('-dateassigned',),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeid', models.AutoField(db_column='EmployeeID', primary_key=True, serialize=False)),
                ('empfirstname', models.CharField(blank=True, db_column='EmpFirstName', max_length=20, null=True)),
                ('emplastname', models.CharField(blank=True, db_column='EmpLastName', max_length=20, null=True)),
                ('dateadded', models.DateField(blank=True, db_column='DateAdded', default=datetime.date.today, null=True)),
                ('empfullname', models.TextField(blank=True, db_column='EmpFullName', null=True)),
                ('department', models.TextField(blank=True, db_column='Department', default='', null=True)),
                ('job', models.TextField(blank=True, db_column='Job', default='', null=True)),
            ],
            options={
                'verbose_name_plural': 'Employees',
                'db_table': 'Employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Searchempinfo',
            fields=[
                ('employeeid', models.IntegerField(db_column='EmployeeID', primary_key=True, serialize=False)),
                ('empfirstname', models.CharField(blank=True, db_column='EmpFirstName', max_length=20, null=True)),
                ('emplastname', models.CharField(blank=True, db_column='EmpLastName', max_length=20, null=True)),
                ('job', models.CharField(blank=True, db_column='Job', max_length=255, null=True)),
                ('department', models.CharField(blank=True, db_column='Department', max_length=255, null=True)),
                ('dateadded', models.DateField(blank=True, db_column='DateAdded', null=True)),
            ],
            options={
                'verbose_name': 'Search Employees',
                'db_table': 'SearchEmpInfo',
                'managed': False,
            },
        ),
    ]
