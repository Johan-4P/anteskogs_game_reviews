from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from  .models import UserGame
from .forms import UserGameForm
from reviews.views import GameList
# Create your views here.

@login_required
def user_games(request):
    games = UserGame.objects.filter(author=request.user)
    return render(request, 'user_games/user_games.html', {'games': games})

@login_required
def edit_game(request, game_id):
    game = get_object_or_404(UserGame, id=game_id)
    if game.author != request.user:
        return redirect('user_games:user_games') 

    if request.method == 'POST':
        form = UserGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('user_games:user_games')
    else:
        form = UserGameForm(instance=game)

    return render(request, 'user_games/edit_game.html', {'form': form, 'game': game})

@login_required
def delete_game(request, game_id):
    game = get_object_or_404(UserGame, id=game_id)
    if game.author != request.user:
        return redirect('user_games:user_games')

    game.delete()
    return redirect('user_games:user_games')