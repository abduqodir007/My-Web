from django.shortcuts import render, redirect
from .models import*
from .models import Student

# Create your views here.
def home(request):
    students = Student.objects.all()  # Barcha talabalarni olish
    return render(request, "index.html",{'students': students})



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

        # Yangi Talaba obyektini yaratish
        student = Student(
            first_name=first_name,
            last_name=last_name,
            father_name=father_name,
            phone_number=phone_number,
            father_phone_number=father_phone_number,
            registration_date=registration_date,
            course_type=course_type
        )
        # Ma'lumotlarni bazaga saqlash
        student.save()

        # Saqlangandan keyin redirect qilish (masalan, 'student_list' sahifasiga)
        return redirect('home')
    
    # GET so'rovida formani render qilish
    return render(request, 'add_student.html')
