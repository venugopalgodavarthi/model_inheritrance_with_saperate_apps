from django.shortcuts import redirect, render
from django.http import HttpResponse
from demo1.models import student
from django.db.models import Q
from django.db.models import Avg,Sum,Count,Min,Max
import datetime
# Create your views here.
def insert(request):
    if request.method=="POST":
        sname =request.POST['sname']
        marks= request.POST['marks']
        doj= request.POST['doj']
        print(sname,marks,doj)
        student.objects.create(sname=sname,marks=marks,doj=doj)
        #return HttpResponse('insert')
        return redirect('select')
    return render(request,'insert.html')


def select(request):
    res=student.objects.all()
    return render(request,'select.html',{'res':res})


def update(request):
    if request.method=='POST':
        sid= request.POST['sid']
        res=student.objects.filter(sid=sid)
        return render(request,'update.html',{'res':res})
    return render(request,'update.html')

def update_value(request,sid):
    if request.method=="POST":
        sname =request.POST['sname']
        marks= request.POST['marks']
        doj= request.POST['doj']
        print(sname,marks,doj)
        res=student.objects.filter(sid=sid).update(sname=sname,marks=marks,doj=doj)
        #return HttpResponse('update')
        return redirect('select')
    return render(request,'insert.html')


def delete(request):
    if request.method=='POST':
        sid= request.POST['sid']
        res=student.objects.filter(sid=sid)
        return render(request,'delete.html',{'res':res})
    return render(request,'delete.html')
95
def delete_value(request,sid):
    if request.method=="POST":
        res=student.objects.filter(sid=sid).delete()
        #return HttpResponse('update')
        return redirect('select')
    
def oper(request):
    #res= student.objects.filter(sid=16,marks=100)    #logical and operator
    #res=student.objects.filter(sid=16) & student.objects.filter(marks=10) #logical and operator
    #res = student.objects.filter(Q(sid=16) & Q(marks=100)) #logical and opertaor
   
    #res= student.objects.filter(marks=100) | student.objects.filter(sid=16)  #logical or opertaor
    #res = student.objects.filter(Q(sid=16) | Q(marks=100))    #logical or opertaor
    
    res = student.objects.exclude(marks=98)    #logical not opertaor
    
    #res = student.objects.exclude(Q(sid=16) | Q(marks=100))   #logical not( or ) opertaor
    
    #res = student.objects.exclude(Q(sid=16) & Q(marks=100))   #logical not( and ) opertaor
    
    return render(request,'select.html',{'res':res})


def reloper(request):
    #res=student.objects.filter(marks__lt=95)  #lessthan
    #res=student.objects.filter(marks__lte=96)  #lessthan or equal
    #res=student.objects.filter(marks__gt=95) #greaterthan
    #res=student.objects.filter(marks__gte=95) #greaterthan or equal
    #res=student.objects.filter(marks=100)  # equal to equal to
    res=student.objects.exclude(marks=100) # not equal
    return render(request,'select.html',{'res':res})

def speoper(request):
    #res= student.objects.filter(marks__in=[100,96,65])
    #res= student.objects.exclude(marks__in=[100,96,65])
    #start_date=datetime.date(1995,1,1)
    #end_date=datetime.date(1996,1,1)
    #res= student.objects.filter(doj__range=(start_date,end_date))
    #res= student.objects.exclude(doj__range=(start_date,end_date))
    #res=student.objects.filter(sname__startswith='S')
    #res=student.objects.filter(sname__istartswith='S')
    #res=student.objects.filter(sname__endswith='I')
    #res=student.objects.filter(sname__iendswith='i')
    #res=student.objects.filter(sname__contains='A')
    res=student.objects.filter(sname__icontains='I')    
    return render(request,'select.html',{'res':res})
    
def order(request):
    #res=student.objects.all().order_by('sname')  #ascending order
    res=student.objects.all().order_by('-sname')  #descending order
    return render(request,'select.html',{'res':res})

def arth(request):
    res=student.objects.get(sid=18)
    res.marks+=10
    res.save()
    return HttpResponse('update')

def arth(request):
    res1=student.objects.all().aggregate(Sum('marks'))
    res2=student.objects.all().aggregate(Avg('marks'))
    res3=student.objects.all().aggregate(Min('marks'))
    res4=student.objects.all().aggregate(Max('marks'))
    res5=student.objects.all().aggregate(Count('marks'))
    return render(request,'select.html',{'res1':res1,'res2':res2,'res3':res3,'res4':res4,'res5':res5})



    