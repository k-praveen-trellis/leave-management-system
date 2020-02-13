from django.shortcuts import render

def login(request):
    return render(request,'accounts/login.html')

def employee(request):
    return render(request,'accounts/employee.html')

def manager(request):
    return render(request,'accounts/manager.html')

def find_user(request):
    
