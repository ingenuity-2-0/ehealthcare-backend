from django.db import models
from doctor.models import Doctor


# Create your models here.
class Hospital(models.Model):
    hospital_id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(verbose_name='Hospital Name', max_length=255, blank=False, null=False)
    city = models.CharField(verbose_name='City', blank=True, null=True, max_length=30)
    address = models.TextField(verbose_name='Hospital Address', blank=True, null=True)
    phone = models.CharField(verbose_name='Contact Number', null=True, blank=True, max_length=100)
    image = models.ImageField(verbose_name='Hospital Image', blank=True, null=True, upload_to='hospital/',
                              default='hospital.png')

    def __str__(self):
        return self.name


class Works(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    start = models.CharField(verbose_name='Consulting Hour Start', max_length=10, null=True, blank=True)
    end = models.CharField(verbose_name='Consulting Hour End', max_length=10, null=True, blank=True)
    fees = models.CharField(verbose_name='Consulting Fees', max_length=10, null=True, blank=True)
    days = models.CharField(verbose_name='Consulting Days', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.hospital_id.name
