from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('employee/',views.employee,name='employee'),
    path('manager/',views.manager,name='manager'),
    path('check/',views.find_user,name='find')
]
