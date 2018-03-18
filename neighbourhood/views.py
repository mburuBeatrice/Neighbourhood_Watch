# from .models import Neighbourhood,Business,User
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
# from django.contrib import messages
# from .forms import NeighbourhoodForm,BusinessForm
# Create your views here.
def index(request):
    # queryset = Neighbourhood.objects.all()
    # query = Business.objects.all()

    # context = {
    #     "object_list":queryset,
    #     "object":query
    # }
    return render(request, 'index.html')

# def find_neighbourhood(request, id):

#     instance = get_object_or_404(Neighbourhood, id=id)
#     context = {
#         "neighbourhood_name":instance.neighbourhood_name,
#         "instance":instance 
#     }
#     return render(request, 'index.html', context)
# def create_neighbourhood(request):
#     form = NeighbourhoodForm(request.POST or None, request.FILES or None)
#     # current_user = request.user
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         messages.success(request, "Successfully created")
#         return HttpResponseRedirect(instance.get_absolute_url())
#     else:
#         messages.error(request, "Not successfully created")


#     context = {
#         "form" : form,
#     }

#     return render(request, 'neighbourhood_form.html', context)

# def update_neighbourhood(request, id=None):
#     instance = get_object_or_404(Neighbourhood, id=id)
#     form = NeighbourhoodForm(request.POST or None,request.FILES or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         messages.success(request, "Post Saved")
#         return HttpResponseRedirect(instance.get_absolute_url())
   

#     context = {

#         "neighbourhood_name":instance.neighbourhood_name,
#         "instance": instance,
#         "form": form,
#     }
    
#     return render(request, 'neighbourhood_form.html', context)

# def delete_neighbourhood(request, id=None):
#     instance = get_object_or_404(Neighbourhood, id=id)
#     instance.delete()
#     messages.success(request, "Post Deleted")
#     return redirect("/")
   
# update_occupants()
# def find_business(request, id):

#     instance = get_object_or_404(Business, id=id)
#     context = {
#         "business_name":instance.business_name,
#         "instance":instance 
#     }
#     return render(request, 'index.html', context)

# def create_business(request):
#     form = BusinessForm(request.POST or None, request.FILES or None)
#     # current_user = request.user
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         messages.success(request, "Successfully created")
#         return HttpResponseRedirect(instance.get_absolute_url())
#     else:
#         messages.error(request, "Not successfully created")


#     context = {
#         "form" : form,
#     }

#     return render(request, 'business_form.html', context)

# def update_business(request, id=None):
#     instance = get_object_or_404(Business, id=id)
#     form = BusinessForm(request.POST or None,request.FILES or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         messages.success(request, "Post Saved")
#         return HttpResponseRedirect(instance.get_absolute_url())
   

#     context = {

#         "business_name":instance.business_name,
#         "instance": instance,
#         "form": form,
#     }
    
#     return render(request, 'business_form.html', context)

# def delete_neighbourhood(request, id=None):
#     instance = get_object_or_404(Neighbourhood, id=id)
#     instance.delete()
#     messages.success(request, "Post Deleted")
#     return redirect("/")
   

