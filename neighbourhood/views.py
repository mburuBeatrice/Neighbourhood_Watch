from .models import Neighbourhood
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib import messages
from .forms import NeighbourhoodForm
# Create your views here.
def index(request):
    queryset = Neighbourhood.objects.all()

    context = {
        "object_list":queryset,
        "neighbourhood_name": "name"
    }
    return render(request, 'index.html',context)

def find_neighbourhood(request, id):

    instance = get_object_or_404(Neighbourhood, id=id)
    context = {
        "neighbourhood_name":instance.neighbourhood_name,
        "instance":instance 
    }
    return render(request, 'index.html', context)
def create_neighbourhood(request):
    form = NeighbourhoodForm(request.POST or None, request.FILES or None)
    # current_user = request.user
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not successfully created")


    context = {
        "form" : form,
    }

    return render(request, 'neighbourhood_form.html', context)

def update_neighbourhood(request, id=None):
    instance = get_object_or_404(Neighbourhood, id=id)
    form = NeighbourhoodForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
   

    context = {

        "neighbourhood_name":instance.neighbourhood_name,
        "instance": instance,
        "form": form,
    }
    
    return render(request, 'neighbourhood_form.html', context)

# def delete_neighbourhood(request, id=None):
#     instance = get_object_or_404(Neighbourhood, id=id)
#     instance.delete()
#     messages.success(request, "Post Deleted")
#     return redirect("post_list")
   
# delete_neigborhood()


# update_neighborhood()
# update_occupants()