from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '📧 Email Address',
            'style': 'padding-left: 30px;',
        })
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🧑 First Name',
            'style': 'padding-left: 30px;',
        })
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🧑 Last Name',
            'style': 'padding-left: 30px;',
        })
    )
    ROLE_CHOICES = (
        (False, 'Patient'),
        (True, 'Doctor')
    )
    is_doctor = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input',
        }),
        label="I am a"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_doctor']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        
        # Username field customization
        self.fields['username'].widget.attrs.update({
            'class': 'form-control mb-3 mt-3 rounded-pill',
            'placeholder': '👤 User Name',
            'style': 'padding-left: 30px;',
        })
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        # Password1 field customization
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🔒 Password',
            'style': 'padding-left: 30px;',
        })
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        # Password2 field customization
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control mb-3 rounded-pill',
            'placeholder': '🔒 Confirm Password',
            'style': 'padding-left: 30px;',
        })
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''

    def save(self, commit=True):
        user = super().save(commit=False)
        is_doctor = self.cleaned_data['is_doctor'] == 'True'
        user.is_doctor = is_doctor
        user.is_patient = not is_doctor
        if commit:
            user.save()
        return user