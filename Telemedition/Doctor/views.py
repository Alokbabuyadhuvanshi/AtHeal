from django.shortcuts import render, redirect
from Doctor.models import Doctor
from django.contrib import messages
from .forms import ConsultForm , DoctorUpdateForm, PasswordUpdateForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def consult_doctor(request):
    doctors = None
    form = ConsultForm()

    if request.method == 'POST':
        form = ConsultForm(request.POST)
        if form.is_valid():
            problem = form.cleaned_data['problem']
            doctors = Doctor.objects.filter(Specialization__icontains=problem)
    
    return render(request, 'Doctor/consult_doctor.html', {
        'form': form,
        'doctors': doctors
    })

@login_required(login_url='/login/')
def update_doctor_info(request):
    doctor = request.user.doctor
    if request.method == 'POST':
        form = DoctorUpdateForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your information has been updated successfully.')
            return redirect('home')
    else:
        form = DoctorUpdateForm(instance=doctor)
    return render(request, 'Doctor/update_doctor_info.html', {'form': form})

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
                    messages.error(request, 'New passwords do not match.')
            else:
                messages.error(request, 'Old password is incorrect.')
    else:
        form = PasswordUpdateForm()
    return render(request, 'update_password.html', {'form': form})
