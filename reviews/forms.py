from django import forms
from .models import Game
from django_summernote.widgets import SummernoteWidget

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'featured_image', 'content', 'status', 'excerpt']
        widgets = {
            'content': SummernoteWidget(),
        }