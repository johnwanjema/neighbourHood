from django import forms
from .models import Post, Profile,Hood,Business

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','email')