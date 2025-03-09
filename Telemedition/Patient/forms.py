from django import forms
from .models import Patient

class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['image', 'Age', 'problems', 'Contact', 'Address']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'Age': forms.NumberInput(attrs={'placeholder': 'Enter your age', 'class': 'form-control'}),
            'problems': forms.Textarea(attrs={'placeholder': 'Describe your medical problems', 'class': 'form-control', 'rows': 3}),
            'Contact': forms.TextInput(attrs={'placeholder': 'Enter your contact number', 'class': 'form-control'}),
            'Address': forms.Textarea(attrs={'placeholder': 'Enter your address', 'class': 'form-control', 'rows': 2}),
        }
        labels = {
            'image': 'Change Profile Image',
            'Age': 'Age',
            'problems': 'Health Problems',
            'Contact': 'Contact Number',
            'Address': 'Address',
        }

class PasswordUpdateForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter current password', 'class': 'form-control'}),
        label='Current Password'
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password', 'class': 'form-control'}),
        label='New Password'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm new password', 'class': 'form-control'}),
        label='Confirm Password'
    )
