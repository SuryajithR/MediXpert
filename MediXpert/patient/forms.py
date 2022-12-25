from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, min_length=2,
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your name'}))
    phone = forms.CharField(label='Phone number', max_length=35, min_length=10,
                             widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Mobile No.'}))
    email = forms.EmailField(label='Email', max_length=35, min_length=5,
                             widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter Email ID'}))
    password1 = forms.CharField(label='Password', max_length=50, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'New Password'}))
    password2 = forms.CharField(label='Confirm Password',
                                max_length=50, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm Password'}))



