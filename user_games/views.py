from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from reviews.models import Game
from .forms import UserGameForm
from django.db.models import Count


@login_required
def user_games(request):
    games = Game.objects.filter(
        author=request.user).annotate(comment_count=Count(
            'comments')).order_by('title')
    return render(request, 'user_games/user_games.html', {'games': games})


@login_required
def edit_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if game.author != request.user:
        return redirect('user_games:user_games')

    if request.method == 'POST':
        form = UserGameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            messages.success(request, "Game updated successfully.")
            return redirect('user_games:user_games')
    else:
        form = UserGameForm(instance=game)

    return render(
        request, 'user_games/edit_game.html', {'form': form, 'game': game})


@login_required
def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if game.author != request.user:
        return redirect('user_games:user_games')

    game.delete()
    messages.success(request, "Game deleted successfully.")
    return redirect('user_games:user_games')
