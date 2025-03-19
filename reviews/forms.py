from django import forms
from .models import Game, Comment
from django_summernote.widgets import SummernoteWidget

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'featured_image', 'content', 'status', 'excerpt']
        widgets = {
            'content': SummernoteWidget(),
        }

    def clean_featured_image(self):
        image = self.cleaned_data.get('featured_image')
        if image and image.size > 5 * 1024 * 1024:  # 5 MB limit
            raise forms.ValidationError("The image size should not exceed 5 MB.")
        return image

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': 'Comment',
        }
