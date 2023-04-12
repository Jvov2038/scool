from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class SchoolClass(models.Model):
    school_class = models.CharField(max_length=10, null=True, blank=True, verbose_name="Учебный класс")

    def __str__(self):
        return self.school_class


class School(models.Model):
    school = models.CharField(max_length=100, null=True, blank=True, verbose_name="Школа")

    def __str__(self):
        return self.school


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    patronymic = models.CharField(max_length=255, null=True, blank=True, verbose_name="Отчество")
    birth = models.DateTimeField(null=True, blank=True, verbose_name="Дата рождения")
    school_class = models.ForeignKey(SchoolClass, on_delete=models.PROTECT, verbose_name="Класс", null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.PROTECT, verbose_name="Школа", null=True, blank=True)
    merit = models.TextField(blank=True, verbose_name="Заслуги", null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name




