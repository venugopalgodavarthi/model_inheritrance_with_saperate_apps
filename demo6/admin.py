from django.contrib import admin
from demo6.models import customer,product,transcation
# Register your models here.


class customeradmin(admin.ModelAdmin):
    list_display=['cid','name','email','phone','address','adhaar']

class productadmin(admin.ModelAdmin):
    list_display=['pid','pname','pdesc','price',]



class transcationadmin(admin.ModelAdmin):
    list_display=['cid','name','email','phone','address','adhaar','pid','pname','pdesc','price','tid','totalprice','date']
    

admin.site.register(transcation,transcationadmin)
admin.site.register(customer,customeradmin)
admin.site.register(product,productadmin)
