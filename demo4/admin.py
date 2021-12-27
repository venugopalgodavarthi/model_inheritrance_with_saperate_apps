from django.contrib import admin
from demo4.models import stu,address,course
# Register your models here.

class stuadmin(admin.ModelAdmin):
    list_display=['firstname','email','phone']
    
class addressadmin(admin.ModelAdmin):
    list_display=['firstname','email','phone','dno','street','city','state','country']
    
class courseadmin(admin.ModelAdmin):
    list_display=['firstname','email','phone','dno','street','city','state','country','courses','marks','fee']
admin.site.register(stu,stuadmin)
admin.site.register(address,addressadmin)
admin.site.register(course,courseadmin)