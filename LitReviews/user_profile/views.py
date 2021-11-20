from itertools import chain
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from feed.models import Ticket, Review
from authentication.models import User
from . import forms


@login_required
def user_profile(request, user):
    user = User.objects.get(username=user)
    user_follows = user.follows.all()
    user_followers = user.followed_by.all()
    tickets = Ticket.objects.filter(user=user.id)
    reviews = Review.objects.filter(user=user.id)

    follow_form = forms.FollowUserButton(initial={'user_to_follow': user.id})
    if request.user.follows.filter(id=user.id).exists():
        btn_text = "Se désabonner"
    else:
        btn_text = "S'abonner"

    if request.method == 'POST':
        follow_form = forms.FollowUserButton(request.POST)
        if follow_form.is_valid():
            user_to_follow = get_object_or_404(User, id=follow_form.cleaned_data['user_to_follow'])
            if request.user.follows.filter(id=user_to_follow.id).exists():
                request.user.follows.remove(user_to_follow)
                user_to_follow.followed_by.remove(request.user)
                btn_text = "S'abonner"
            else:
                request.user.follows.add(user_to_follow)
                user_to_follow.followed_by.add(request.user)
                btn_text = "Se désabonner"

    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    context = {
        'follow_form': follow_form,
        'btn_text': btn_text,
        'requested_user': user,
        'user_follows': user_follows,
        'user_followers': user_followers,
        'tickets_and_reviews': tickets_and_reviews
    }

    return render(
        request,
        'user_profile/user_profile.html',
        context
    )


@login_required
def update_profile_photo(request):
    form = forms.UpdateProfilePhoto(instance=request.user)
    if request.method == 'POST':
        form = forms.UpdateProfilePhoto(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(request.user.username + '/')
    context = {
        'form': form
    }
    return render(
        request,
        'user_profile/update_profile_photo.html',
        context
    )


@login_required
def followers_page(request, user):
    search_form = forms.SearchUser()
    searched_user_resp = ""
    requested_user = User.objects.get(username=user)
    # search
    searched_user_resp_btn = ''

    # get follows and followers
    user_follows = requested_user.follows.all()
    user_followers = requested_user.followed_by.all()

    group_follows_users = {}
    for user in user_follows:
        follow_form = forms.FollowUserButton(initial={'user_to_follow': user.id})
        group_follows_users[user] = follow_form

    if request.method == 'POST':

        # search form
        if request.POST.get('search_user_id'):
            search_form = forms.SearchUser(request.POST)
            if search_form.is_valid():
                query = search_form.cleaned_data['search']
                searched_user = User.objects.filter(username__icontains=query).first()
                if searched_user:
                    searched_user_resp = searched_user
                    searched_user_resp_btn = forms.FollowUserButton(initial={'user_to_follow': searched_user.id})

        # follow / unfollow button
        else:
            follow_form = forms.FollowUserButton(request.POST)
            if follow_form.is_valid():
                user_to_follow = get_object_or_404(User, id=follow_form.cleaned_data['user_to_follow'])
                if request.user.follows.filter(id=user_to_follow.id).exists():
                    request.user.follows.remove(user_to_follow)
                    user_to_follow.followed_by.remove(request.user)
                else:
                    request.user.follows.add(user_to_follow)
                    user_to_follow.followed_by.add(request.user)

    context = {
        'search_form': search_form,
        'searched_user_resp': searched_user_resp,
        'searched_user_btn': searched_user_resp_btn,
        'requested_user': requested_user,
        'user_follows': user_follows,
        'group_user_follows': group_follows_users,
        'user_followers': user_followers
    }
    return render(
        request,
        'user_profile/followers.html',
        context
    )