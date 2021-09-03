from django.db import models
from doctor.models import Specialist


# Create your models here.
class Symptoms(models.Model):
    symptom = models.TextField(verbose_name='Symptoms', blank=False, null=False)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)

    def __str__(self):
        return self.symptom
