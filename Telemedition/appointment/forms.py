from django import forms
from django.utils import timezone
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'notes','file']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'min': timezone.now().strftime('%Y-%m-%dT%H:%M')
            }),
            'notes': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Additional notes for the doctor...'
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf, .jpg, .png',
            }),
        }