from itertools import chain
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from feed.models import Ticket, Review
from authentication.models import User
from . import forms


@login_required
def user_profile(request, user):
    user = User.objects.get(username=user)
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
                btn_text = "S'abonner"
            else:
                request.user.follows.add(user_to_follow)
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

