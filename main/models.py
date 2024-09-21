from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)  # Ismi
    last_name = models.CharField(max_length=100)   # Familiyasi
    father_name = models.CharField(max_length=100)  # Otasining ismi
    phone_number = models.CharField(max_length=30)  # O'zining telefon nomeri
    father_phone_number = models.CharField(max_length=30)  # Otasining telefon nomeri
    registration_date = models.DateField()  # Ro'yxatdan o'tgan sana
    course_type = models.CharField(max_length=100)  # Kurs turi
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)  # To'lanadigan summa
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Chegirma foizi
    final_payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Yakuniy to'lov

    def calculate_final_payment(self):
        # Chegirma asosida yakuniy to'lovni hisoblash
        if self.discount_percent > 0:
            discount_amount = (self.payment_amount * self.discount_percent) / 100
            self.final_payment = self.payment_amount - discount_amount
        else:
            self.final_payment = self.payment_amount

    def save(self, *args, **kwargs):
        # Yakuniy to'lovni avtomatik hisoblash
        self.calculate_final_payment()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
