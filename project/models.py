from django.db import models

class runners(models.Model):
    first_name = models.CharField('first name', max_length=100)
    last_name = models.CharField('last name', max_length=100)
    gender = models.CharField('gender', max_length=1)
    finish_time = models.CharField('finish time', max_length=10)
