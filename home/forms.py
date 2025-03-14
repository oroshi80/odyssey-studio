from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    # Add any custom validation if needed
    def clean_message(self):
        message = self.cleaned_data.get('message')
        # Example: Ensuring message is not empty or too short
        if len(message) < 10:
            raise forms.ValidationError("Message is too short. Please provide more details.")
        return message
