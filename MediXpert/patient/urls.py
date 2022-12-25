from django.urls import path
from . import views

app_name = "patient"

urlpatterns=[
    path('home/', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.create_user, name='register'),

    path('doctor/', views.doctorList, name='doctor'),
    # path('doctorbook/<int:id>/', views.doctorBook, name='doctorbook'),
    path('doctorbook/', views.doctorList, name='doctorbook'),
    path('bookdoctor/<int:id>', views.doctorBook, name='bookdoctor'),
    path('appointment/', views.appointment, name='appointment'),
    path('profile/', views.profile, name='profile'),
    path('user/', views.user, name='user'),
    path('report/<int:id>', views.report, name='report'),
]