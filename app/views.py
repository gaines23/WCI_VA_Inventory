"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, reverse
from django.template import loader, Context
from django.http import HttpRequest
from .models import *
from .forms import *
from django.db.models import Count
from django.forms import ModelForm, inlineformset_factory
from django.views.generic import View, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .filters import *




def home(request):
    assert isinstance(request, HttpRequest)
    return render(request,
                  'app/index.html',
                 
    )


# Landing page to Add new Employee, Search Emp, or Add Dept/Job

def EmployeeLanding(request):
    assert isinstance(request, HttpRequest)

    empsearch = Searchempinfo.objects.all()
    emps = Employee.objects.all()

     # POST new Employee information
    if request.method == 'POST' and 'emp' in request.POST:
        empinfoform = EmpInfoForm(request.POST)

        if empinfoform.is_valid():
            empinfoform.save()
        else:
            empinfoform = EmpInfoForm()
            return HttpResponseRedirect("/EmployeeLanding/")
    else:
        empinfoform = EmpInfoForm()

    
    context = {'search':empsearch,
               'empinfoform':empinfoform,
               'emps':emps,
               }

    return render(request,
                  'app/employee/EmployeeLanding.html',
                  context,
    )


# Page details employee info; can add new garms to EmpID
def EmployeeDetails(request, employeeid):
    assert isinstance(request, HttpRequest)

    extra_forms = 0

    EditGarmFormSet = inlineformset_factory(
        Employee, Assignempgarm, form=AssignGarmForm,
        fields = ["garmtype", "garmsize", "dateassigned", "quantity", "replacement", ],
        fk_name = 'employeeid',
        extra = extra_forms,
        can_delete = True,
    )

    empinfo = Employee.objects.get(employeeid=employeeid)
    deptjob = Employee.objects.all()


    # Query to update Employee info on Form 
    if request.method == 'POST' and 'edit' in request.POST:
        empinfoform = EmpInfoForm(request.POST, instance=empinfo)

        if empinfoform.is_valid():
            empinfoform.save()
            return HttpResponseRedirect("/EmployeeDetails/"+employeeid)
        else:
            empinfoform = EmpInfoForm(instance=empinfo)
    else:
        empinfoform = EmpInfoForm(instance=empinfo)


    # Deletes Employee from database
    if request.method == 'POST' and 'delete' in request.POST:
        empinfo.delete()
        return HttpResponseRedirect("/EmployeeLanding/")


    # Assigns new garments to Employee    
    if request.method == 'POST' and 'assign' in request.POST:
        formset = EditGarmFormSet(request.POST, instance=empinfo)
        
        if formset.is_valid():
            for i in range(0, formset.total_form_count()):
                form = formset.forms[i]
                form.save()
            formset.save()
            return HttpResponseRedirect("/EmployeeDetails/"+employeeid)

    else:
        formset = EditGarmFormSet(instance=empinfo)


    context = {'empinfoform':empinfoform, 
               'empinfo':empinfo,
               'deptjob':deptjob,
               'formset':formset,
               }

    return render(request, 
                  'app/employee/EmployeeDetails.html',
                  context,
    )

