from .models import ContactMeForm
from django import forms


class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMeForm
        fields = ('name', 'email', 'message')
