from django.urls import path
from . import views

app_name = "patient"

urlpatterns=[
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('consult/<int:id>/', views.consult, name='consult'),
    path('addDetails/', views.addDetails, name='addDetails'),
]