from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from patient.models import *
from doctor.models import *
from .models import *

# Create your views here.


def home(request):
    patients = testResult.objects.all()
    return render(request,'labhome.html', {"patients":patients})

def logout_user(request):
    logout(request)
    return redirect('index')

def consult(request, id):
    patients = get_object_or_404(testResult, tid=id)
    return render(request,'consult.html', {"patients":patients})

def addDetails(request):
    if request.method == "POST":
        id = request.POST['tid']
        post = get_object_or_404(testResult, tid=id)
        post.bloodp = request.POST['trestbps']
        post.chol = request.POST['chol']
        post.fasting = request.POST['fbs']
        post.ecg = request.POST['restecg']
        post.cpain = request.POST['exang']
        post.cpaintype = request.POST['cp']
        post.heart = request.POST['thalach']
        post.status=False
        post.save()

        return redirect('lab:home')
    else:
        return redirect('lab:addDetails')

