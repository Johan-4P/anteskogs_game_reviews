from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError

# Maximum image size
MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5MB

# Validator function
def validate_image_size(image):
    if image.size > MAX_IMAGE_SIZE:
        raise ValidationError("The image file is too large. Maximum size is 5MB.")

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Game(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False, null=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games_posts')
    featured_image = CloudinaryField('image', blank=True, null=True, validators=[validate_image_size])  # Add validator here
    content = models.TextField(blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(max_length=100, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField(blank=False, null=False)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
