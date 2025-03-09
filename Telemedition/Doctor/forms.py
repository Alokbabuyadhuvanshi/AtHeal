from django import forms
from .models import Doctor

class ConsultForm(forms.Form):
    problem = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter specialization...'
        }),
        label="Consult Doctor:"
    )

class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['image', 'Specialization', 'Qualification', 'Experience', 'Contact', 'Address']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'Specialization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter specialization'}),
            'Qualification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter qualifications'}),
            'Experience': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter years of experience'}),
            'Contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
            'Address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter address'}),
        }
        labels = {
            'image': 'Change Profile Image',
            'Specialization': 'Specialization',
            'Qualification': 'Qualification',
            'Experience': 'Experience (in years)',
            'Contact': 'Contact Number',
            'Address': 'Clinic Address'
        }

class PasswordUpdateForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter old password'
        }),
        label="Old Password"
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter new password'
        }),
        label="New Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm new password'
        }),
        label="Confirm Password"
    )
