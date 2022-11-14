from django.urls import path
from . import views

app_name = "patient"

urlpatterns=[
    path('home/', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.create_user, name='register'),

    path('doctor/', views.doctor_details, name='doctor'),
]