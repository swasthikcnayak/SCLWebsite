import re

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserUpdateForm, ProfileUpdateForm, UserRegisterForm
from .models import Profile, Request
from teams.models import Teams


def register(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'authorization/register.html', context)


def user_login(request):
    if request.POST:
        user_cred = request.POST['username']
        password = request.POST['password']
        if email_check(user_cred):
            username = User.objects.get(email=user_cred).username
            user = authenticate(request, username=username, password=password)
        else:
            user = authenticate(request, username=user_cred, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged into your account!!')
            return redirect('home')

        else:
            messages.error(request, 'Invalid Credential')
            return redirect(request.META['HTTP_REFERER'])
    else:
        return render(request, 'authorization/login.html', {'title': "Login"})


@login_required
def profile(request):
    user = get_object_or_404(User, id=request.user.id)
    mentor = get_object_or_404(Profile, user__id=user.id)
    requested_sessions = Request.objects.filter(mentor=mentor, status='1')
    completed_sessions = Request.objects.filter(mentor=mentor, status='2')
    profile_details = {}
    if request.POST:
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Your Account has been Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user.profile)

        query = Profile.objects.filter(user__id=user.id).first()
        profile_details = {
            'username': query.user.username,
            'batch': query.batch,
            'name': query.name,
            'phone': query.phone,
            'college': query.college,
            'degree': query.degree,
            'branch': query.branch,
            'profession': query.profession,
            'guidance': query.guidance,
        }
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': "Profile",
        'profile_details': profile_details,
        'requested_sessions': requested_sessions,
        'completed_sessions': completed_sessions
    }
    return render(request, 'profile/profile.html', context=context)


def mentors_list(request):
    mentors = Profile.objects.filter(role='2')
    return render(request, 'mentors/mentors_list.html', {'mentors': mentors})


def request_time(request, mentor_id):
    requesting_user = request.user
    requesting_profile = get_object_or_404(Profile, user__id=requesting_user.id)
    requesting_team = get_object_or_404(Teams, id=requesting_profile.team.id)
    mentor = get_object_or_404(Profile, user__id=mentor_id)
    Request(requested_by=requesting_profile, team=requesting_team, mentor=mentor).save()
    messages.success(request,
                     f'Your request for the session is booked with {mentor.name}, please expect the response soon.')
    return redirect('home')


def completed_session(request, request_id):
    record = get_object_or_404(Request, id=request_id)
    record.status = '2'
    record.save()
    messages.success(request, f'Your session is marked booked and is be removed from list')
    return redirect('profile')


def incompleted_session(request, request_id):
    record = get_object_or_404(Request, id=request_id)
    record.status = '1'
    record.save()
    messages.success(request, f'Your session is marked incomplete and is added to the list')
    return redirect('profile')


def email_check(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    else:
        return None
