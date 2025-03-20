from django import forms
from .models import Game, Comment
from django_summernote.widgets import SummernoteWidget
from cloudinary.api import resource  # Import Cloudinary Admin API

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'featured_image', 'content', 'status', 'excerpt']
        widgets = {
            'content': SummernoteWidget(),
        }

    def clean_featured_image(self):
        image = self.cleaned_data.get('featured_image')
        if image:
            try:
                # Use Cloudinary Admin API to get image metadata
                image_metadata = resource(image.public_id)
                file_size = image_metadata.get('bytes', 0)  # File size in bytes

                if file_size > 5 * 1024 * 1024:  # 5 MB limit
                    raise forms.ValidationError("The image size should not exceed 5 MB.")
            except Exception as e:
                raise forms.ValidationError(f"An error occurred while validating the image: {e}")
        return image

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': 'Comment',
        }
