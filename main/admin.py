from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'father_name', 'phone_number', 'father_phone_number', 'registration_date', 'course_type')
