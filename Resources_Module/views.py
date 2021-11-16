from django.forms.formsets import formset_factory
from django.http.response import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
# importing required views
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from Resources_Module.forms import AddHospitalForm, BookingForm, UpdateHospitalForm, UpdateResourceForm

from .models import Hospital, Resource

resource_fields = (
    "icu_beds","remdesivir","vaccine", "ventilators", "hospital"
)

hospital_fields = (
    "name", "address", "phonenumber", "image"
)

# Create your views here.
def index(request):
    return render(request, 'Resources_Module/index.html')


# create view
class add_hospital(CreateView):
    # defining which model to use
    model = Hospital

    form_class = AddHospitalForm

    # defining which template to show 
    template_name = "Resources_Module/add_hospital.html"

    # defining object name for easy access
    context_object_name = "hospital"

    # if added successfully, redirect to list view
    success_url = reverse_lazy("resources-add")


# create view
class add_resource(CreateView):
    # defining which model to use
    model = Resource

    # defining what fields to be filled
    fields = resource_fields

    # defining which template to show 
    template_name = "Resources_Module/add_resource.html"

    # defining object name for easy access
    context_object_name = "resource"

    # if added successfully, redirect to list view
    success_url = reverse_lazy("resources-list")


# read view
class show_hospital_details(DetailView):
    # defining which model to use
    model = Hospital

    # defining which template to show 
    template_name = "Resources_Module/show_hospital_details.html"

    # defining object name for easy access
    context_object_name = "hospital"


# update view
class update_resource(UpdateView):

    model = Resource

    form_class = UpdateResourceForm

    # defining which template to show 
    template_name = "Resources_Module/update_resource.html"

    # defining object name for easy access
    context_object_name = "resource"

    # if added successfully, redirect to list view
    success_url = reverse_lazy("resources-list")


class update_hospital(UpdateView):
    # defining which model to use
    model = Hospital

    form_class = UpdateHospitalForm

    # defining which template to show 
    template_name = "Resources_Module/update_hospital.html"

    # defining object name for easy access
    context_object_name = "hospital"        

    # if added successfully, redirect to list view
    success_url = reverse_lazy("resources-list")

# # delete view
class delete_resource(DeleteView):
    # defining which model to use
    model = Resource

    # defining which template to show 
    template_name = "Resources_Module/delete_resource.html"

    # defining object name for easy access
    context_object_name = "resource"

    # if added successfully, redirect to list view
    success_url = reverse_lazy("resources-list")

class delete_hospital(DeleteView):
    # defining which model to use
    model = Hospital

    # defining which template to show 
    template_name = "Resources_Module/delete_hospital.html"

    # defining object name for easy access
    context_object_name = "hospital"

    # if added successfully, redirect to list view
    success_url = reverse_lazy("resources-list")


# list students view
class list_resources(ListView):
    # defining which model to use
    model = Resource

    # defining which template to show 
    template_name = "Resources_Module/list_resources.html"

    # defining object name for easy access
    context_object_name = "resources"

def book_resource(request, pk):

    resource = Resource.objects.get(hospital_id = pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, pk = pk)

        if form.is_valid():
            icu_beds_needed = form.cleaned_data['icu_beds']
            remdesivir_needed = form.cleaned_data['remdesivir']
            vaccine_needed = form.cleaned_data['vaccine']
            ventilators_needed = form.cleaned_data['ventilators']

            resource.icu_beds -= icu_beds_needed
            resource.remdesivir -= remdesivir_needed
            resource.vaccine -= vaccine_needed
            resource.ventilators -= ventilators_needed

            resource.save()

            return render(request, 'Resources_Module/booking_confirmed.html', {'resource': resource, 'form': form})

    form = BookingForm(pk = pk)
    return render(request, 'Resources_Module/book_resource.html',{'form': form, 'resource_pk': pk, 'resource': resource})