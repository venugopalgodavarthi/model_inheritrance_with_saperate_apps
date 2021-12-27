from django.urls import path
from demo1 import views
urlpatterns=[
    path('insert/',views.insert,name='insert'),
    path('select/',views.select,name='select'),
    path('update/',views.update,name='update'),
    path('update_value/<sid>/',views.update_value,name='update_value'),
    path('delete/',views.delete,name='delete'),
    path('delete_value/<sid>/',views.delete_value,name='delete_value'),
    path('oper/',views.oper,name='oper'),
    path('reloper/',views.reloper,name='reloper'),
    path('speoper/',views.speoper,name='speoper'),
    path('order/',views.order,name='order'),
    path('arth/',views.arth,name='arth'),
]