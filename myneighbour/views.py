from django.shortcuts import render, redirect,get_object_or_404
from .models import Post, Profile, Hood, Business
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, NeighbourhoodForm,NewBusinessForm
# Create your views here.


def welcome(request):
    neighbourhoods = Hood.objects.all()
    return render(request, 'index.html', {"neighbourhoods": neighbourhoods, })


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


@login_required(login_url='/accounts/login/')
def addneighbourhood(request):
    neighbourform = NeighbourhoodForm()
    if request.method == "POST":
        neighbourform = NeighbourhoodForm(request.POST, request.FILES)
        if neighbourform.is_valid():
            neighbourform.save()
            return redirect('welcome')
        else:
            neighbourform = NeighbourhoodForm(request.POST, request.FILES)
    return render(request, 'hood.html', {"neighbourform": neighbourform})


@login_required(login_url="/accounts/login/")
def new_business(request,pk):
    current_user = request.user
    neighborhood = get_object_or_404(Hood,pk=pk)
    if request.method == 'POST':
        business_form = NewBusinessForm(request.POST, request.FILES)
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.user = current_user
            business.neighborhood=neighborhood
            business.save()
        return redirect('detail', neighbourhood_id=neighborhood.id)

    else:
        business_form = NewBusinessForm()
    return render(request, 'new_business.html', {"form": business_form,'neighborhood':neighborhood})

@login_required(login_url="/accounts/login/")
def hood_details(request,neighbourhood_id):
    businesses=Business.objects.filter(hood=neighbourhood_id)
    posts=Post.objects.filter(neighbourhood=neighbourhood_id)
    neighbourhood=Hood.objects.get(pk=neighbourhood_id)
    return render(request,'hood_details.html',{'neighbourhood':neighbourhood,'businesses':businesses,'posts':posts})
