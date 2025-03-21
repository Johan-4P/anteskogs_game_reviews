from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.db.models import Count, Q
from .models import Game, Comment
from django.http import Http404
from .forms import GameForm, CommentForm
import logging

logger = logging.getLogger(__name__)


class HomeView(TemplateView):
    template_name = 'reviews/home.html'


class GameList(generic.ListView):
    template_name = 'reviews/index.html'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Game.objects.filter(
                status=1
            ).filter(
                Q(title__icontains=query) | Q(excerpt__icontains=query)
            ).annotate(comment_count=Count('comments')).order_by('-created_on')
        else:
            return Game.objects.filter(
                status=1
            ).annotate(comment_count=Count('comments')).order_by('-created_on')


class GameDetail(generic.DetailView):
    template_name = 'reviews/review_detail.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        game = get_object_or_404(Game, slug=slug)
        if game.status == 0 and game.author != self.request.user:
            raise Http404("Game not found")
        return game

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = self.get_object()
        comments = game.comments.filter(approved=True)
        pending_comments = game.comments.filter(approved=False)
        user_comments_pending = pending_comments.filter(
            author=self.request.user
            ) if self.request.user.is_authenticated else []

        context["comments"] = comments
        context["pending_comments_count"] = pending_comments.count()
        context["user_comments_pending"] = user_comments_pending
        context["comment_count"] = comments.count()
        context["comment_form"] = CommentForm()
        return context


@login_required
def upload_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        
        # Check if the form is valid
        if form.is_valid():
            try:
                game = form.save(commit=False)
                game.author = request.user
                game.slug = slugify(game.title)

                # Check if an image was uploaded; handle accordingly
                if not request.FILES.get('image'):
                    game.image = None  # You can set a default image or leave it as None
                
                game.save()
                messages.success(request, "Game uploaded successfully.")
                return redirect('reviews')

            except Exception as e:
                logger.error(f"Error saving game: {e}")
                form.add_error(None, "An error occurred while saving the game.")
        else:
            logger.error("Form is not valid")
            return render(request, 'reviews/upload_game.html', {'form': form})
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
            messages.success(
                request, "Comment submitted and awaiting approval.")
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
    return render(
        request, "reviews/edit_comment.html",
        {"form": form, "comment": comment})


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

    return render(
        request, "reviews/edit_game.html", {"form": form, "game": game})


@login_required
def delete_game(request, slug):
    game = get_object_or_404(Game, slug=slug)

    if game.author != request.user:
        messages.error(request, "You are not allowed to delete this game.")
        return redirect('review_detail', slug=game.slug)

    game_slug = game.slug
    game.delete()
    messages.success(request, "Game deleted successfully.")
    return redirect('reviews')


def thanks(request):
    return render(request, 'about/thanks.html')
