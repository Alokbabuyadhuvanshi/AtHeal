from django.db import models
from Doctor.models import Doctor
from Patient.models import Patient

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('⌛', '⌛'),
        ('✔', '✔'),
        ('✖', '✖'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='⌛')
    notes = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='appointment_files/', blank=True, null=True)
    video_call_room = models.CharField(max_length=100, blank=True, null=True)  # Store Room ID
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.user} -> {self.doctor.user} ({self.get_status_display()})"
