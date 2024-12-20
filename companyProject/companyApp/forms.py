from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from companyApp.models import User
from .models import Employee

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class CustomPasswordChangeForm(PasswordChangeForm):
    pass 

from django import forms
from companyApp.models import Employee

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['position', 'department', 'salary']  # Fields that can be updated by the admin

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'position', 'department', 'salary']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

