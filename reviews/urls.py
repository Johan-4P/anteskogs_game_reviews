from django.urls import path
from . import views

urlpatterns = [
    path('', views.GameList.as_view(), name='reviews'),
    path('upload/', views.upload_game, name='upload_game'),  # Move this line before the slug pattern
    path('<slug:slug>/', views.GameDetail.as_view(), name='review_detail'),
]