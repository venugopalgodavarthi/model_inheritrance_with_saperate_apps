from django.contrib import admin
from demo5.models import details, facutly, student
# Register your models here.


class detailsadmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','address','adhaar']
    
admin.site.register(details,detailsadmin)


class facultyadmin(admin.ModelAdmin):
    list_display=['details_ptr_id','name','email','phone','address','adhaar','course','salary']
    
admin.site.register(facutly,facultyadmin)

class studentadmin(admin.ModelAdmin):
    list_display=['details_ptr_id','name','email','phone','address','adhaar','course','marks','fee']
    
admin.site.register(student,studentadmin)
