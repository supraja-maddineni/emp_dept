from django.shortcuts import render
from app.models import *
# Create your views here.

def display_depttable(request):
    LOD=DEPT_Table.objects.all()
    LOD=DEPT_Table.objects.filter(dname__startswith='a')
    LOD=DEPT_Table.objects.all()

    d={'dept':LOD}
    return render(request,'display_depttable.html',context=d)

def display_emptable(request):
    LOE=EMP_Table.objects.all()
    LOE=EMP_Table.objects.filter(ename__startswith='a')
    LOE=EMP_Table.objects.filter(ename__startswith='s')
    LOE=EMP_Table.objects.all()
    LOE=EMP_Table.objects.filter(ename__endswith='s')
    LOE=EMP_Table.objects.all()
    LOE=EMP_Table.objects.filter(job__endswith='s')
    LOE=EMP_Table.objects.all()
    LOE=EMP_Table.objects.filter(ename__contains='l')
    LOE=EMP_Table.objects.filter(hiredate__year='1980')
    LOE=EMP_Table.objects.filter(hiredate__year__lte='1980')
    LOE=EMP_Table.objects.filter(hiredate__year__gt='1981')
    LOE=EMP_Table.objects.all()
    LOE=EMP_Table.objects.filter(mgr__contains='8')
    LOE=EMP_Table.objects.all()
    LOE=EMP_Table.objects.filter(ename__in=('allen','miller'))

    d={'empl':LOE}
    return render(request,'display_emptable.html',context=d)
