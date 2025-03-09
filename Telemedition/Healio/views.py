from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from Doctor.models import Doctor
from Patient.models import Patient
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Check if the user selected Doctor or Patient
            if user.is_doctor:
                Doctor.objects.create(user=user)
            elif user.is_patient:
                Patient.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            if user.is_doctor:
                return redirect('update_doctor_info')
            else:
                return redirect('update_patient_info')
            
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, ("Login successful..."))
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, ("You have been logged out..."))
    return redirect('login')


def about(request):
    return render(request,'about.html')
