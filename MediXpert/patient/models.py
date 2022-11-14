from datetime import datetime
from django.db import models


class Patient(models.Model):
    username = models.CharField(max_length=30)
    dateofb = models.CharField(max_length=30)
    gender = models.CharField(max_length=50)
    phone_num = models.IntegerField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=30, default='patient')

    def __str__(self):
        return self.username


class LabAssist(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=30, default='lab')

    def __str__(self):
        return self.full_name


class Doctor(models.Model):
    full_name = models.CharField(max_length=30)
    desig = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=30, default='doc')

    def __str__(self):
        return self.full_name
