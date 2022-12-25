from django.urls import path
from . import views

app_name = "patient"

urlpatterns=[
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('viewpatients/', views.viewPatients, name='viewpatients'),
    path('refer/', views.refer, name='refer'),
    path('stopconsult/<int:id>', views.stopConsult, name='stopconsult'),
    path('diagnose', views.diagnose, name='diagnose'),
    path('predict/<int:id>', views.predict, name='predict'),
    path('model/<int:id>', views.model, name='model'),
]