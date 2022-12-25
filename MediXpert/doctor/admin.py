from django.contrib import admin
from patient.models import *

# Register your models here.
@admin.register(DBook)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['id','uname','dname','bdate','btime', 'age', 'gender', 'uid', 'status', 'refer']

admin.site.register(DBookFinish)