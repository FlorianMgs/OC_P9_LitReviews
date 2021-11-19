from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UpdateProfilePhoto(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_photo']


class FollowUserButton(forms.Form):
    user_to_follow = forms.CharField(widget=forms.HiddenInput())
