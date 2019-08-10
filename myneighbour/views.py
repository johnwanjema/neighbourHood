from django.shortcuts import render,redirect
from .models import Post, Profile,Hood,Business
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
# Create your views here.
def welcome(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user)
    print(profile)
    my_profile = Profile.objects.get(user=current_user)
    return render(request, 'profile.html', locals())


@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = current_user
            prof.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm()
    return render(request, 'update_profile.html', {'form': form})