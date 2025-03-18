from django.urls import path, include
from . import views
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('reviews/', views.GameList.as_view(), name='game_reviews_search'),
    path('list/', views.GameList.as_view(), name='reviews'),
    path('upload/', views.upload_game, name='upload_game'),
    path('<slug:slug>/', views.GameDetail.as_view(), name='review_detail'),
    path('<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('game/edit/<slug:slug>/', views.edit_game, name='edit_game'),
    path('game/delete/<slug:slug>/', views.delete_game, name='delete_game'),
]
