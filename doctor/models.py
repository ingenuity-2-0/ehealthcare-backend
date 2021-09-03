from django.db import models


# Create your models here.
class Specialist(models.Model):
    id = models.CharField(verbose_name='ID', primary_key=True, max_length=8)
    name = models.CharField(verbose_name='Specialist Name', max_length=30, null=False)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    doctor_id = models.CharField(primary_key=True, max_length=8, verbose_name='Doctor ID')
    name = models.CharField(verbose_name='Doctor Name', blank=False, null=False, max_length=100)
    qualification = models.TextField(verbose_name='Qualification', max_length=450, blank=True, null=True)
    designation = models.TextField(verbose_name='Designation', max_length=450, blank=True, null=True)
    specialist_name = models.ForeignKey(Specialist, verbose_name='Specialist Name', on_delete=models.CASCADE)
    # work = models.ManyToOneRel(Works, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctors/', blank=True, null=True, default='doctors.png')

    def __str__(self):
        return self.name
