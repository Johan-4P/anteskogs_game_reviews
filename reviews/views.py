from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Game
# Create your views here.

class GameList(generic.ListView):
    queryset = Game.objects.filter(status=1)
    template_name = 'reviews/index.html'
    paginate_by = 6


class GameDetail(generic.DetailView):
    """
    This view will display the detailed view of a single game.
    """
    queryset = Game.objects.filter(status=1)
    template_name = 'reviews/review_detail.html'

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        return get_object_or_404(queryset, slug=slug)
