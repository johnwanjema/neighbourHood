from django import forms
from .models import Post, Profile,Hood,Business

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','email')

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model=Hood
        exclude = ['admin']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['name','hood','email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']