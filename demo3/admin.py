from django.contrib import admin
from demo3.models import dept,employee
# Register your models here.

class deptadmin(admin.ModelAdmin):
    list_display=['id','dname','location']
    
class employeeadmin(admin.ModelAdmin):
    list_display=['id','firstname', 'email', 'phone', 'address', 'aadhar','d' ]

admin.site.register(dept,deptadmin)
admin.site.register(employee,employeeadmin)

