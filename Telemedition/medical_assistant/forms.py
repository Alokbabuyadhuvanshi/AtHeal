from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea( attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Describe your symptoms or health question...',
                'rows': '2',
                'id': 'user-input'
            }),
            required=True,
            label='',
    )
    