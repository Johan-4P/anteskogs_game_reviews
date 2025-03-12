from django.urls import path
from . import views

app_name = 'user_games'

urlpatterns = [
    path('', views.user_games, name='user_games'),
    path('edit/<int:game_id>/', views.edit_game, name='edit_game'),
]
