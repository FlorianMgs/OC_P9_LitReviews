from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View
from django.conf import settings

from . import forms


class LoginPage(View):
    form_class = forms.LoginForm
    template_name = 'authentication/login.html'

    def get(self, request):
        form = self.form_class
        message = ''
        context = {
            'form': form,
            'message': message
        }
        return render(
            request,
            self.template_name,
            context
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('feed')

        message = 'Identifiants invalides.'
        context = {
            'form': form,
            'message': message
        }
        return render(
            request,
            self.template_name,
            context
        )


class SignupPage(View):
    form_class = forms.SignupForm
    template_name = 'authentication/signup.html'

    def get(self, request):
        form = self.form_class
        context = {
            'form': form
        }
        return render(
            request,
            self.template_name,
            context
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        context = {
            'form': form
        }
        return render(
            request,
            self.template_name,
            context
        )


def logout_user(request):
    logout(request)
    return redirect('login')
