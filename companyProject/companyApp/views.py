from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import User, Employee
from .serializers import EmployeeSerializer, UserSerializer
from django.http import HttpResponseForbidden
from django.contrib import messages
from companyApp.forms import UserUpdateForm, CustomPasswordChangeForm, EmployeeUpdateForm 
from .forms import EmployeeForm, UserForm
from django.contrib.auth.decorators import user_passes_test


# API Views
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# HTML Views
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('admin_dashboard' if user.is_admin else 'employee_dashboard')
        return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        return redirect('employee_dashboard')
    employees = Employee.objects.all()
    return render(request, 'admin_dashboard.html', {'employees': employees})

@login_required
def employee_dashboard(request):
    if request.user.is_admin:
        return redirect('admin_dashboard')
    user = request.user
    try:
        employee = Employee.objects.get(user=user)
    except Employee.DoesNotExist:
        employee = None 
    
    return render(request, 'employee_dashboard.html', {
        'user': user,
        'employee': employee
    })

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@login_required
def edit_profile(request):
    user = request.user

    # Initialize forms
    form = UserUpdateForm(instance=user)
    password_form = CustomPasswordChangeForm(user)

    if request.method == 'POST':
        if 'update_details' in request.POST:
            form = UserUpdateForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your details were updated successfully.')
                return redirect('edit_profile')
        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Keeps the user logged in after password change
                messages.success(request, 'Your password was updated successfully.')
                return redirect('edit_profile')
            else:
                messages.error(request, 'Please correct the error below.')

    return render(request, 'edit_profile.html', {
        'form': form,
        'password_form': password_form,
    })


# Ensure only admin users can access this view
def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    # Ensure the user is an admin (staff member) before allowing employee modification
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to edit employees.")
        return redirect('employee_list')
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=employee.user)
        employee_form = EmployeeForm(request.POST, instance=employee)

        if user_form.is_valid() and employee_form.is_valid():
            user_form.save()
            employee_form.save()
            messages.success(request, "Employee details updated successfully!")
            return redirect('companyApp.admin_dashboard')
    else:
        user_form = UserForm(instance=employee.user)
        employee_form = EmployeeForm(instance=employee)

    return render(request, 'edit_employee.html', {
        'user_form': user_form,
        'employee_form': employee_form,
        'employee': employee
    })

# View for listing employees
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

# View for creating a new employee
@login_required
def create_employee(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        
        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save()
            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()
            messages.success(request, "Employee created successfully!")
            return redirect('employee_list')
    else:
        user_form = UserForm()
        employee_form = EmployeeForm()
    
    return render(request, 'create_employee.html', {'user_form': user_form, 'employee_form': employee_form})     

@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    # Ensure the user is an admin (staff member) before allowing deletion
    if request.user.is_staff:
        employee.delete()
        messages.success(request, "Employee deleted successfully!")
        return redirect('employee_list')
    else:
        messages.error(request, "You do not have permission to delete employees.")
        return redirect('employee_list')
