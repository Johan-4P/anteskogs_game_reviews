from django.urls import path
from . import views


app_name = 'user_games'  # Ensure the app name is set


urlpatterns = [
    path('', views.user_games, name='user_games'),
]
