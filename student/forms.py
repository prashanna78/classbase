from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student
from django.forms import ModelForm

class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','address','email']

