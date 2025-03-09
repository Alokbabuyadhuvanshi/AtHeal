from django.shortcuts import render, get_object_or_404, redirect
from Doctor.models import Doctor
from Patient.models import Patient
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import uuid


@login_required(login_url='/login/')
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    patient = get_object_or_404(Patient, user=request.user)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)

        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.patient = patient
            appointment.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('consult_doctor')
    else:
        form = AppointmentForm()
    
    return render(request, 'Appointment/book_appointment.html', {
        'form': form,
        'doctor': doctor
    })

@login_required(login_url='/login/')
def doctor_appointments(request):
    if not hasattr(request.user, 'doctor'):
        return redirect('consult_doctor')
        
    doctor = request.user.doctor
    appointments = Appointment.objects.filter(doctor=doctor).order_by('-appointment_date')
    return render(request, 'Appointment/appointments.html', {
        'appointments': appointments
    })

@login_required(login_url='/login/')
def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['⌛', '✔', '✖']:
            appointment.status = status
            appointment.save()
            messages.success(request, 'Appointment status updated!')
        return redirect('doctor_appointments')
    
    return render(request, 'Appointment/update_appointment.html', {
        'appointment': appointment
    })

@login_required(login_url='/login/')
def patient_appointments(request):
    if not hasattr(request.user, 'patient'):
        messages.error(request, "You are not registered as a patient.")
        return redirect('home')

    patient = request.user.patient
    appointments = Appointment.objects.filter(patient=patient).order_by('-appointment_date')

    return render(request, 'Appointment/patient_appointments.html', {
        'appointments': appointments
    })


@login_required
def start_video_call(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id, doctor=request.user.doctor)

    # Generate unique room ID
    room_id = str(uuid.uuid4())  
    appointment.video_call_room = room_id
    appointment.save()

    return redirect(f'/appointment/video_call/?roomID={room_id}')

@login_required
def video_call(request):
    appointment = Appointment.objects.filter(video_call_room=request.GET.get('roomID')).first()
    return render(request, 'Appointment/Video_call.html', {
        'Username': request.user.get_full_name,
        'appointment': appointment  
    })

@login_required
def end_video_call(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # clear The UUID once the video all end 
    if request.user == appointment.doctor.user: # can only done by Doctor
        appointment.video_call_room = None
        appointment.save()

    return redirect('doctor_appointments')  # Redirect to the doctor’s appointment page
