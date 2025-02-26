from django.shortcuts import render
from django.views import generic
from .models import Game
# Create your views here.

class GameList(generic.ListView):
    queryset = Game.objects.filter(status=1)
    template_name = 'reviews/index.html'
    paginate_by = 6
