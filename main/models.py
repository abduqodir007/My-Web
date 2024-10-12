
from django.db import models
from decimal import Decimal  # Decimal ishlatish tavsiya qilinadi

class Student(models.Model):
    first_name = models.CharField(max_length=100)  # Ismi
    last_name = models.CharField(max_length=100)   # Familiyasi
    father_name = models.CharField(max_length=100)  # Otasining ismi
    phone_number = models.CharField(max_length=30)  # O'zining telefon nomeri
    father_phone_number = models.CharField(max_length=30)  # Otasining telefon nomeri
    registration_date = models.DateField()  # Ro'yxatdan o'tgan sana
    course_type = models.CharField(max_length=100)  # Kurs turi
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)  # To'lanadigan summa
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Chegirma summasi
    final_payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Yakuniy to'lov

    def calculate_final_payment(self):
        # Chegirma asosida yakuniy to'lovni hisoblash
        payment_amount = Decimal(self.payment_amount)  # Stringdan Decimal ga aylantirish
        discount = Decimal(self.discount_amount) if self.discount_amount else Decimal(0)  # Stringdan Decimal ga aylantirish

        self.final_payment = payment_amount - discount  # Yakuniy to'lovni hisoblash