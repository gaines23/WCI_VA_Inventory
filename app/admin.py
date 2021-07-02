from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import AdminSite
from .models import *

# Register Models Here

##### TABLES #####
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employeeid", "empfirstname", "emplastname", 
                    "dateadded", "empfullname", 
                    "department", "job", )
admin.site.register(Employee, EmployeeAdmin)

class AssigngarmAdmin(admin.ModelAdmin):
    list_display = ("employeeid", "garmentid", "dateassigned",
                    "quantity", "replacement", "garmsize", 
                    "garmtype",)
admin.site.register(Assignempgarm, AssigngarmAdmin)


##### VIEWS #####
class SearchEmpAdmin(admin.ModelAdmin):
    list_display = ("employeeid", "empfirstname", "emplastname", "job", 
                    "department", "dateadded", )
admin.site.register(Searchempinfo, SearchEmpAdmin)
