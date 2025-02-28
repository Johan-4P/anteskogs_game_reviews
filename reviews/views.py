from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Game
from .forms import GameForm
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
    

@login_required
def upload_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.author = request.user
            game.slug = slugify(game.title)  # Automatically generate the slug
            game.save()
            return redirect('reviews')  # Redirect to the reviews page
    else:
        form = GameForm()
    return render(request, 'reviews/upload_game.html', {'form': form})


