from django.contrib import admin
from django.db.models import Sum
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # Ko'rsatiladigan ustunlar ro'yxati
    list_display = ('first_name', 'last_name', 'father_name', 'phone_number', 'father_phone_number', 'registration_date', 'course_type', 'final_payment')

    # Custom admin view for total payments and student count
    # change_list_template = 'admin/student_changelist.html'

    def changelist_view(self, request, extra_context=None):
        # Barcha talabalarning soni va yakuniy to'lovlar hisobini olish
        extra_context = extra_context or {}
        student_count = Student.objects.count()  # Hamma studentlar soni
        total_final_payment = Student.objects.aggregate(Sum('final_payment'))['final_payment__sum']  # Yakuniy to'lov summasi

        # Agar final_payment qiymati null bo'lsa, uni 0 ga almashtirish
        if total_final_payment is None:
            total_final_payment = 0

        extra_context['student_count'] = student_count
        extra_context['total_final_payment'] = total_final_payment

        # Asosiy changelist view'ni chaqirish va qo'shimcha ma'lumotlar qo'shish
        return super().changelist_view(request, extra_context=extra_context)
