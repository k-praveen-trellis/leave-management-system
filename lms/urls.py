from django.urls import path,include
from accounts import views

urlpatterns = [
    path('',views.login,name="home_login")
]
