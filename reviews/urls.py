from django.urls import path
from . import views

urlpatterns = [
    path('', views.GameList.as_view(), name='reviews'),
    path('<slug:slug>/', views.GameDetail.as_view(), name='review_detail'),
]