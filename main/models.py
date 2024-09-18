from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)  # Ismi
    last_name = models.CharField(max_length=100)   # Familiyasi
    father_name = models.CharField(max_length=100)  # Otasining ismi
    phone_number = models.CharField(max_length=30)  # Ozining telefon nomeri
    father_phone_number = models.CharField(max_length=30)  # Otasining telefon nomeri
    registration_date = models.DateField()  # Registratsiya qilingan sana
    course_type = models.CharField(max_length=100)  # Kurs turi

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
