# Generated by Django 5.1.1 on 2024-09-16 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('father_phone_number', models.CharField(max_length=15)),
                ('registration_date', models.DateField()),
                ('course_type', models.CharField(max_length=100)),
            ],
        ),
    ]
