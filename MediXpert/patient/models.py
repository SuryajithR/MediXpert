from datetime import datetime
from django.db import models


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    phone_num = models.IntegerField(default=0)
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
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=30)
    desig = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=30, default='doc')

    def __str__(self):
        return self.full_name


class DBook(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=30)
    uid = models.IntegerField()
    dname = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    bdate = models.DateField()
    btime = models.CharField(max_length=30)
    refer = models.BooleanField(default=True)
    status = models.BooleanField(default=True)


class DBookFinish(models.Model):
    bid = models.IntegerField()
    uname = models.CharField(max_length=30)
    uid = models.IntegerField()
    dname = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    bdate = models.DateField()
    btime = models.CharField(max_length=30)
    refer = models.BooleanField(default=True)
    status = models.BooleanField(default=True)


class testResult(models.Model):
    tid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=30)
    uid = models.IntegerField()
    bid = models.IntegerField()
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    bloodp = models.IntegerField(default=0)
    chol = models.IntegerField(default=0)
    fasting = models.CharField(max_length=30,default="NULL")
    ecg = models.CharField(max_length=100,default="NULL")
    heart = models.IntegerField(default=0)
    cpain = models.CharField(max_length=30,default="NULL")
    cpaintype = models.CharField(max_length=200,default="NULL")
    status = models.BooleanField(default=True)







