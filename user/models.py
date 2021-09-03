from django.db import models


# Create your models here.
class User(models.Model):
    f_name = models.CharField(verbose_name='First Name', max_length=30, null=False, blank=False)
