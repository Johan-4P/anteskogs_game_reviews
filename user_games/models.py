from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserGame(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title