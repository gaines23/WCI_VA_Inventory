"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *
import json
from datetime import date
from django.forms.widgets import NumberInput


# Add/Edit Employee Form
class EmpInfoForm(forms.ModelForm):
    dateadded = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), initial=date.today, required=False)

    class Meta:
        model = Employee
        fields = ["employeeid", "empfirstname", "emplastname", "dateadded", 
                  "empfullname", "department", "job", ]


class AssignGarmForm(forms.ModelForm):
    dateassigned = forms.DateField(widget=NumberInput(attrs={'type': 'date', 'class': 'dateassigned'}), initial=date.today)
    replacement = forms.ChoiceField(choices=Assignempgarm.repChoices)
    garmtype = forms.CharField(widget=forms.Textarea(attrs={"rows":1, "cols":15, 'class': 'garmtype'}))
    garmsize = forms.CharField(widget=forms.TextInput(attrs={'class':'garmsize'}))
    quantity = forms.CharField(widget=forms.TextInput(attrs={'class':'quantity'}))

    class Meta:
        model = Assignempgarm
        fields = ["dateassigned", "quantity", "replacement", "garmsize", "garmtype", ]
