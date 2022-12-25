from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from datetime import datetime
from django.utils import timezone
from django.core.mail import send_mail


def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'home.html', {'doctors':doctors})
    # return render(request,'home.html')

def doctor_details(request):
    return render(request,'doctors.html')

def login_user(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)
            if user.check_password("Doc@1234"):
                login(request, user)
                redirect_url = request.GET.get('next', 'doctor:home')
                return redirect(redirect_url)
            elif user.check_password("Doc2@1234"):
                login(request, user)
                redirect_url = request.GET.get('next', 'doctor:home')
                return redirect(redirect_url)
            elif user.check_password("Lab@1234"):
                login(request, user)
                redirect_url = request.GET.get('next', 'lab:home')
                return redirect(redirect_url)
            elif user is not None:
                login(request, user)
                redirect_url = request.GET.get('next', 'patient:home')
                return redirect(redirect_url)
            else:
                messages.warning(request, "Incorrect Username/Password!")
                return render(request, 'login.html')

    except AttributeError:
        messages.warning(request, "Incorrect Username/Password!")
        return render(request, 'login.html')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('index')


def create_user(request):
    if request.method == 'POST':
        check1 = False
        check2 = False
        check3 = False
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']

            if password1 != password2:
                check1 = True
                messages.error(request, 'Password did not match!',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if User.objects.filter(username=username).exists():
                check2 = True
                messages.error(request, 'Username already exists!',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if User.objects.filter(email=email).exists():
                check3 = True
                messages.error(request, 'Email already registered!',
                               extra_tags='alert alert-warning alert-dismissible fade show')

            if check1 or check2 or check3:
                messages.error(
                    request, "Registration Failed!", extra_tags='alert alert-warning alert-dismissible fade show')
                return redirect('patient:register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                messages.success(
                    request, f'Thanks for registering {user.username}.', extra_tags='alert alert-success alert-dismissible fade show')
                acc=Patient()
                acc.username = form.cleaned_data['username']
                acc.phone_num = form.cleaned_data['phone']
                acc.email = form.cleaned_data['email']
                acc.password= form.cleaned_data['password1']

                acc.save()
                print("user_created")
                return redirect('patient:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'reg.html', {'form': form})


def profile(request):  
    name = request.user
    appoints = DBook.objects.all().filter(uname=name,  status=1)  
    pastappoints = DBookFinish.objects.all().filter(uname=name,  status=0) 
    # stat=pastappoints.status
    # if stat == 0:
    #     stat = "Consultation successfll"
    # else:
    #     stat = "Consultation successfll"
    return render(request, 'profile.html', {"appoints":appoints, "pastappoints":pastappoints})

def user(request):  
    name = request.user
    user = User.objects.all().filter(username=name)  
    d = request.user.date_joined
    dt = datetime(2022, 12, 21, 12, 34, 56)
    date = dt.date()
    return render(request, 'user.html', {"user":user,"date":date})


def doctorList(request):        
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors':doctors})

def report(request, id):    
    name = request.user
    reports = testResult.objects.all().filter(bid=id)  
    return render(request, 'report.html', {'reports':reports})


def doctorBook(request,id):    
    uname = request.user
    iid = request.user.id
    doctors = get_object_or_404(Doctor, pk=id)
    return render(request, 'doctorbook.html', {"doctors":doctors,"name":uname, "iid":iid})

def appointment(request):
    uname = request.user
    docname = request.POST['dname']
    user = User.objects.all().filter(username=uname)  
    uemail = request.user.email
    doctors = get_object_or_404(Doctor, full_name=docname)
    if request.method == "POST":
        uuid = request.user.id
        doc = request.POST['dname']
        bdat = request.POST['date']
        time = request.POST['time']

        date_string = bdat
        date_format = "%Y-%m-%d"
        date = datetime.strptime(date_string, date_format)
        date = timezone.make_aware(date)

        appointments_on_date = DBook.objects.filter(dname=doc, bdate=date, btime=time)

        if appointments_on_date.exists():
            print("appointment already there")
            
            messages.error(request, "Doctor not available !!!")
            messages.error(request, "Select a different date/time")
            # return redirect('patient:doctorbook')
            return render(request, 'doctorbook.html', {"doctors":doctors,"name":uname,"iid":uuid})
        else:
            post=DBook()
            post.uname = request.POST['pname']
            post.dname = request.POST['dname']
            post.age = request.POST['age']
            post.gender = request.POST['inlineRadioOptions']
            post.bdate = request.POST['date']
            post.btime = request.POST['time']
            post.uid = request.POST['iid']
            post.save()
            messages.success(request, "Appointment has taken")

            usname = str(uname)
            subject = "Appointment Confirmation MediXpert"
            message = "Hi, "+usname+",   You recently scheduled an appointment for "+bdat+" at "+time+". The appointment has been confirmed successfully. Please reply to this email if you’d like to cancel or reschedule the appointment."

            # send_mail(subject, message, 'sr.mca2123@saintgits.org', [uemail], fail_silently=False)

            return render(request, 'home.html')
    else:
        return redirect('patient:doctorbook')
