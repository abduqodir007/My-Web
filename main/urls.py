from django.urls import path
from .views import*


urlpatterns = [
    path("", addstudent, name="addstudent"),
    path("home/", home, name="home"),
    path('admin_panel/', student_list, name='student_list'),  
]