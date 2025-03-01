from django.urls import path
from . import views

urlpatterns = [
    path('', views.GameList.as_view(), name='reviews'),
    path('upload/', views.upload_game, name='upload_game'),
    path('<slug:slug>/', views.GameDetail.as_view(), name='review_detail'),
    path('<slug:slug>/comment/', views.add_comment, name='add_comment'),
]