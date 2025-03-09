from django.shortcuts import render, redirect
from .models import Patient
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PatientUpdateForm, PasswordUpdateForm

@ login_required(login_url='/login/')
def Update_patient_info(request):
    patient = request.user.patient
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your information has been updated successfully.')
            return redirect('home')
    else:
        form = PatientUpdateForm(instance=patient)
    return render(request, 'Patient/update_patient_info.html', {'form': form})
    
@login_required(login_url='/login/')
def update_password(request):
    if request.method == 'POST':
        form = PasswordUpdateForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']
            if request.user.check_password(old_password):
                if new_password == confirm_password:
                    request.user.set_password(new_password)
                    request.user.save()
                    messages.success(request, 'Your password has been updated successfully.')
                    return redirect('login')
                else:
                    messages.error(request, ' New passwords do not match.')
            else:
                messages.error(request,'Old password is incorrect.')
    else:
        form = PasswordUpdateForm()
    return render(request, 'update_password.html', {'form': form})

            
