from django import forms
from .models import UserGame

class UserGameForm(forms.ModelForm):
    class Meta:
        model = UserGame
        fields = ['title', 'description']