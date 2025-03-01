from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Game, Comment
from .forms import GameForm, CommentForm
import logging

logger = logging.getLogger(__name__)

class GameList(generic.ListView):
    queryset = Game.objects.filter(status=1)
    template_name = 'reviews/index.html'
    paginate_by = 6


class GameDetail(generic.DetailView):
    queryset = Game.objects.filter(status=1)
    template_name = 'reviews/review_detail.html'

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        return get_object_or_404(queryset, slug=slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = self.get_object()
        comments = game.comments.filter(approved=True)
        comment_count = comments.count()
        context["comments"] = comments
        context["comment_count"] = comment_count
        context["comment_form"] = CommentForm()  # Add the comment form to the context
        return context
    

@login_required
def upload_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                game = form.save(commit=False)
                game.author = request.user
                game.slug = slugify(game.title)  # Automatically generate the slug
                game.save()
                return redirect('reviews')  # Redirect to the reviews page
            except Exception as e:
                logger.error(f"Error saving game: {e}")
                form.add_error(None, "An error occurred while saving the game.")
        else:
            logger.error("Form is not valid")
    else:
        form = GameForm()
    return render(request, 'reviews/upload_game.html', {'form': form})


@login_required
def add_comment(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.game = game
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment submitted and awaiting approval.")
            return redirect("review_detail", slug=game.slug)

    else:
        messages.error(request, "Invalid request.")
        return redirect("review_detail", slug=game.slug)


