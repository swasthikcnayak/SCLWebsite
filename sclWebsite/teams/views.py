from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from .models import Teams
from .forms import TeamUpdateForm
from users.models import Profile


@login_required
def all_team(request):
    teams = Teams.objects.all().order_by('id')
    context = {
        'teams': teams
    }
    return render(request, 'teams/teams.html', context=context)


@login_required
def single_team(request, team_id):
    user = get_object_or_404(User, id=request.user.id)
    team = Teams.objects.filter(id=team_id).first()
    team_members = Profile.objects.filter(team__id=team.id)
    if user.profile.role == 1:
        return render(request, 'teams/team.html', {'team': team, 'members': team_members})

    if request.POST and user.profile.role == 2:
        team_update_form = TeamUpdateForm(request.POST, instance=team)
        if team_update_form.is_valid():
            team_update_form.save()
            messages.success(request, f'Team has been Updated')
            return redirect('team', team_id=team_id)

    team_update_form = TeamUpdateForm(instance=team)
    context = {
        'team': team,
        'form': team_update_form,
        'members': team_members
    }
    return render(request, 'teams/team.html', context=context)
