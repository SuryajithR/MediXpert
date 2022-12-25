from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from patient.models import *
from .models import *
from sklearn.preprocessing import MinMaxScaler
import joblib
import os
import numpy as np
import pickle
import csv
from datetime import datetime
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request,'dhome.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def diagnose(request):
    name = request.user.get_short_name()
    patients = DBook.objects.all().filter(dname=name)  
    return render(request, 'diagnose.html', {"patients":patients})

def viewPatients(request):
    name = request.user.get_short_name()
    patients = DBook.objects.all().filter(dname=name)  
    return render(request, 'patients.html', {"patients":patients})

def refer(request):
    if request.method == "POST":
        uname = request.POST['uname']
        uid = request.POST['uid']
        age = request.POST['age']
        gender = request.POST['gender']
        id = request.POST['bid']

        post=testResult()
        post.uname = uname
        post.uid = uid
        post.bid = id
        post.age = age
        post.gender = gender
        post.save()

        dname = request.user.get_short_name()
        book = get_object_or_404(DBook, id=id)
        book.refer = False
        book.save()

        return redirect('doctor:viewpatients')
    else:
        return redirect('doctor:viewpatients')


def stopConsult(request, id):
    dname = request.user.get_short_name()
    book = get_object_or_404(DBook, id=id)
    book.status = False
    book.save()
    doc = request.user.get_short_name()
    records = DBook.objects.all().filter(id=id)
    for record in records:
        DBookFinish.objects.create(
            bid=record.id,
            uname=record.uname,
            dname=record.dname,
            age=record.age,
            gender=record.gender,
            bdate=record.bdate,
            btime=record.btime,
            uid=record.uid,
            refer=record.refer,
            status=record.status
        )

        # Retrieve a record
        # rec = DBook.objects.get(dname=doc)
        DBook.objects.filter(id=id).delete()

        # Delete the record
        # rec.delete()
        return redirect('doctor:diagnose')


def predict(request, id):
    books = get_object_or_404(testResult, bid=id)
    records = testResult.objects.all().filter(bid=id)
    if books.status == False:
        return render(request,'predict.html', {"records":records, "books":books}) # Lab report added
    else:
        messages.error(request, "Lab report not available!!!")
        return redirect('doctor:diagnose') # Lab report not added


def model(request, id):
    b = get_object_or_404(testResult, bid=id)
    age = b.age
    sex = b.gender
    trestbps = b.bloodp
    chol = b.chol
    restecg = b.ecg
    thalach = b.heart
    exang = b.cpain
    cp = b.cpaintype
    fbs = b.fasting
    x = np.array([age, sex, cp, trestbps, chol, fbs, restecg,
                  thalach, exang]).reshape(1, -1)

    scaler_path = os.path.join('static\models\scaler.pkl')

    scaler = None

    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)

    x = scaler.transform(x)

    model_path = os.path.join('static\\models\\rfc.sav')
    clf = joblib.load(model_path)

    y = clf.predict(x)
   
    return render(request,'predict.html', {'y':int(y)})



    