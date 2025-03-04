from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.db.models import Count
from .models import Game, Comment
from .forms import GameForm, CommentForm
import logging

logger = logging.getLogger(__name__)

class HomeView(TemplateView):
    template_name = 'reviews/home.html'


class GameList(generic.ListView):
    template_name = 'reviews/index.html'
    paginate_by = 6

    def get_queryset(self):
        return Game.objects.filter(status=1).annotate(comment_count=Count('comments'))


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
        context["comment_form"] = CommentForm() 
        return context
    

@login_required
def upload_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                game = form.save(commit=False)
                game.author = request.user
                game.slug = slugify(game.title)  
                game.save()
                return redirect('reviews') 
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


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        messages.error(request, "You are not allowed to edit this comment.")
        return redirect('review_detail', slug=comment.game.slug)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully.")
            return redirect("review_detail", slug=comment.game.slug)
    else:
        form = CommentForm(instance=comment)
    
    return render(request, "reviews/edit_comment.html", {"form": form, "comment": comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        messages.error(request, "You are not allowed to delete this comment.")
        return redirect('review_detail', slug=comment.game.slug)
    
    game_slug = comment.game.slug
    comment.delete()
    messages.success(request, "Comment deleted successfully.")
    return redirect("review_detail", slug=game_slug)

@login_required
def edit_game(request, slug):
    game = get_object_or_404(Game, slug=slug)
    
    
    if game.author != request.user:
        messages.error(request, "You are not allowed to edit this game.")
        return redirect('review_detail', slug=game.slug)

    if request.method == "POST":
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            messages.success(request, "Game updated successfully.")
            return redirect("review_detail", slug=game.slug)
    else:
        form = GameForm(instance=game)

    return render(request, "reviews/edit_game.html", {"form": form, "game": game})

