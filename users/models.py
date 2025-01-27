from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone_number = models.CharField(max_length=14, blank=True)
    experience = models.PositiveIntegerField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, blank=True)
    salary = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if self.experience >= 1 and self.experience <= 3:
            self.salary = 'Ваша зарплата составляет 1000$'
        elif 3 < self.experience <= 7:
            self.salary = 'Ваша зарплата составляет 2000$'
        elif 7 < self.experience <= 10:
            self.salary = 'Ваша зарплата составляет 5000$'
        else:
            self.salary = 'Опыт работы не соответствует требованиям'

        super().save(*args, **kwargs)
