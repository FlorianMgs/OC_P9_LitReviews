from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms, models


@login_required
def feed(request):
    tickets = models.Ticket.objects.all()
    context = {
        'tickets': tickets
    }
    return render(
        request,
        'feed/feed.html',
        context
    )


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.image = form.cleaned_data['image']
            ticket.save()
            return redirect('feed')
    context = {
        'form': form
    }
    return render(
        request,
        'feed/create_ticket.html',
        context
    )


