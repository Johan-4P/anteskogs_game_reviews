from django.urls import path
from . import views

urlpatterns = [
    path('', views.GameList.as_view(), name='reviews'),
]