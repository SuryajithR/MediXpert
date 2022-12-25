from django.contrib import admin
from patient.models import *

# Register your models here.

@admin.register(testResult)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['uname','uid','tid','bid','age','gender','bloodp', 'chol', 'fasting', 'ecg', 'cpain', 'cpaintype', 'heart','status']

