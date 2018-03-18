from .models import Neighbourhood,Business,UserProfile,Contacts
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NeighbourhoodForm,BusinessForm,NewPostForm
# Create your views here.
def index(request):
    hoods = Neighbourhood.objects.all()
    businesses = Business.objects.all()
    posts = Posts.objects.all()
    context = {
        "hoods":hoods,
        "businesses": businesses,
        "posts": posts
    }
    return render(request, 'index.html', context)
def profile(request, id):

    profile = get_object_or_404(UserProfile, id=id)
    context ={
        "new_profile": profile
    }
    return render(request, 'profile.html', context)
def find_neighbourhood(request, id):

    hood = get_object_or_404(Neighbourhood, id=id)
    context = {
        "hood": hood,
    
    }
    return render(request, 'search.html', context)

def find_contact(request):

    contact = Contacts.objects.all()
    context = {
        "contact": contact
    }
    return render(request, 'contact.html', context)


@login_required(login_url='/accounts/login/')
def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST or None, request.FILES or None)
        # current_user = request.user
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()
            messages.success(request, "Successfully created")
            return redirect('/')
    else:
        messages.error(request, "Not successfully created")

    context = {
        "form" : form,
    }

    return render(request, 'new_post.html', context)
@login_required(login_url='/accounts/login/')
def new_neighbourhood(request):
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST or None, request.FILES or None)
        # current_user = request.user
        if form.is_valid():
            new_neighbourhood = form.save(commit=False)
            new_neighbourhood.save()
            messages.success(request, "Successfully created")
            return redirect('/')
    else:
        messages.error(request, "Not successfully created")

    context = {
        "form" : form,
    }

    return render(request, 'new_post.html', context)
def find_business(request,):

    instance = get_object_or_404(Business, id=id)
    context = {
        "business_name":instance.business_name,
        "instance":instance 
    }
    return render(request, 'index.html', context)

