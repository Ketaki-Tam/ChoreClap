from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('list1', views.list1 , name='list1'),
    path('employee_form' , views.employee_form , name='employee_form'),
    path('about' , views.about , name='about'),
    path('thank' , views.thank , name='thank')
]   