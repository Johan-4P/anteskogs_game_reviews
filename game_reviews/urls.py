"""
URL configuration for game_reviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from reviews import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/games/', include('user_games.urls', namespace='user_games')),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('about/', include('about.urls'), name='about-urls'),
    path('thanks/', views.thanks, name='thanks'),
    path('', views.HomeView.as_view(), name='home'),  # Ensure home view is defined
    path('reviews/', include('reviews.urls')),  # Include reviews URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
