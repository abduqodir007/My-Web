from django.shortcuts import render, redirect
from .models import Student

# Home view: barcha talabalarni ko'rsatish va umumiy to'lovlarni hisoblash
def home(request):
    students = Student.objects.all()  # Barcha talabalarni olish
    total_students = students.count()  # Talabalar soni
    total_payment = sum(student.final_payment for student in students if student.final_payment)  # Yakuniy to'lovlar umumiy summasi

    return render(request, "index.html", {
        'students': students,
        'total_students': total_students,
        'total_payment': total_payment,
    })

# Add Student view: talaba qo'shish va to'lovni hisoblash
def addstudent(request):
    if request.method == 'POST':
        # Formdan kelayotgan ma'lumotlarni o'qib olish
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        father_name = request.POST.get('father_name')
        phone_number = request.POST.get('phone_number')
        father_phone_number = request.POST.get('father_phone_number')
        registration_date = request.POST.get('registration_date')
        course_type = request.POST.get('course_type')
        payment_amount = request.POST.get('payment_amount')
        discount_percent = request.POST.get('discount_percent')

        # Yangi talaba obyektini yaratish
        student = Student(
            first_name=first_name,
            last_name=last_name,
            father_name=father_name,
            phone_number=phone_number,
            father_phone_number=father_phone_number,
            registration_date=registration_date,
            course_type=course_type,
            payment_amount=payment_amount,
            discount_percent=discount_percent
        )
        
        # Yakuniy to'lovni hisoblash
        student.calculate_final_payment()
        
        # Ma'lumotlarni bazaga saqlash
        student.save()

        # Saqlangandan keyin 'home' sahifasiga qaytish
        return redirect('home')
    
    # GET so'rovida formani render qilish
    return render(request, 'add_student.html')

def student_list(request):
    # Barcha talabalarni olish va shablon bilan render qilish
    students = Student.objects.all()  # Immutability printsipiga ko'ra, bu ob'ekt o'zgarmaydi.
    
    # Barcha ma'lumotlar shablon orqali yuboriladi
    return render(request, 'admin.html', {'students': students})