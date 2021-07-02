import django_filters
from .models import *
#from django.db.models import Q

# Employee Landing Search
class EmpSearchFilter(django_filters.FilterSet):
    class Meta:
        model = Searchempinfo
        fields = ['empfirstname', 'emplastname', 'job', 'department']
