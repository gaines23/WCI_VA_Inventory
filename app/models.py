from django.db import models
from datetime import date, datetime



#### TABLES ####
class Employee(models.Model):
    employeeid = models.AutoField(db_column='EmployeeID', primary_key=True)  
    empfirstname = models.CharField(db_column='EmpFirstName', max_length=20, blank=True, null=True)  
    emplastname = models.CharField(db_column='EmpLastName', max_length=20, blank=True, null=True)  
    dateadded = models.DateField(db_column='DateAdded', blank=True, null=True, default=date.today)  
    empfullname = models.TextField(db_column='EmpFullName', blank=True, null=True)  
    department = models.TextField(db_column='Department', blank=True, null=True, default="")
    job = models.TextField(db_column='Job', blank=True, null=True, default="")

    class Meta:
        managed = False
        db_table = 'Employee'
        unique_together = (('employeeid', 'empfullname'))
        ordering = ('-dateadded',)
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.empfullname



class Assignempgarm(models.Model):
    repChoices = (
        ('No', 'No'),
        ('Yes', 'Yes')
    )

    employeeid = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='EmployeeID', blank=True, null=True, related_name='emp', related_query_name='emp')    
    garmentid = models.AutoField(db_column='GarmentID', primary_key=True)    
    dateassigned = models.DateField(db_column='DateAssigned', blank=True, null=True, default=date.today) 
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True, default=" ")
    replacement = models.CharField(db_column='Replacement', max_length=10, blank=True, null=True, choices=repChoices)
    garmtype = models.CharField(db_column='GarmType', max_length=255, blank=True, null=True, default=" ")
    garmsize = models.CharField(db_column='GarmSize', max_length=20, blank=True, null=True, default=" ")

    class Meta:
        managed = False
        db_table = 'AssignEmpGarm'
        ordering = ('-dateassigned',)

    def emp_name(self):
        return self.employeeid.empfullname

    def garm_name(self):
        return self.garmentid





#### VIEWS ####
class Searchempinfo(models.Model):
    employeeid = models.IntegerField(db_column='EmployeeID', primary_key=True)
    empfirstname = models.CharField(db_column='EmpFirstName', max_length=20, blank=True, null=True)   
    emplastname = models.CharField(db_column='EmpLastName', max_length=20, blank=True, null=True)   
    job = models.CharField(db_column='Job', max_length=255, blank=True, null=True)   
    department = models.CharField(db_column='Department', max_length=255, blank=True, null=True)   
    dateadded = models.DateField(db_column='DateAdded', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SearchEmpInfo'
        verbose_name = 'Search Employees'

