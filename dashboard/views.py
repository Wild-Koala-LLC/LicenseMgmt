from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from .models import License, Soldier, Machine
from .helper_funcs import *
from .forms import NameForm, TestForm, LicenseForm
from .resources import LicenseResource

import csv


def csv_view(request):
    license_resource = LicenseResource()
    dataset = license_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="LicenseManger.csv"'
    return response


def delete(request,license_id):
    to_delete = License.objects.get(id=license_id)
    license_name = to_delete.name
    to_delete.delete()
    return redirect('license_details', license_name)

# User Chart.js to make a pie chart with % of a type of license used vs. Not used
def index(request):
    
    unique = get_unique_licenses()
    license_dict = get_used_and_unused(unique) 
    print(license_dict) 

    # get the urls to go to for details, have to have underscores instead of spaces.
    good_urls = []
    for thing in unique:
        good_urls.append(thing.replace(" ", "_"))
    print(good_urls)

    labels = ['Available', 'In Use']

    context = {'labels':labels, 'license_dict':license_dict, 'good_urls':good_urls}
    return render(request, 'pie_chart.html', context)

def assigned(request):
    soldier_list = Soldier.objects.order_by('name')
    machine_list = Machine.objects.order_by('serial_number')
    license_list = License.objects.order_by('-pub_date')
    context = {'soldier_list':soldier_list, 'machine_list':machine_list, 'license_list':license_list}
    return render(request, 'assigned.html', context)

def assign_licenses(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = LicenseForm(request.POST)
        if form.is_valid():
            print("GOT VALID LICENSE!==============================================")
            form.save()
            return redirect('/')

    form = LicenseForm()
    context = {'form':form}
    return render(request, 'assign_licenses.html', context)

def edit(request, license_id):
    to_edit = License.objects.get(id=license_id)
    redirect_name = to_edit.name
    if request.method == 'POST':
        form = LicenseForm(request.POST)
        if form.is_valid():
            print("EDITED LICENSE!==============================================")
            print("================= Deleting Old License ====================")
            to_edit.delete()
            form.save()

            return redirect('license_details', redirect_name)

    form = LicenseForm(initial={'name': to_edit.name, 
                                'key': to_edit.key, 
                                'start_date': to_edit.start_date, 
                                'end_date': to_edit.end_date,
                                'on_machine': to_edit.on_machine})

    context = {'form':form, 'to_edit':to_edit}
    return render(request, 'edit_license.html', context)

def license_details(request, wanted_license):
    
    licenses = License.objects.filter(name=wanted_license)
    green, amber, red = classify_by_time(licenses)
    context = {'wanted_license':wanted_license, 'green':green, 'amber':amber, 'red':red}
    return render(request, 'license_details.html', context)


def expiring(request):
    # this correctly orders the licenses.
    licenses = License.objects.order_by('end_date')

    print("In epiring=======================================")
    for l in licenses:
        print(l)

    # want to return a list to each of these, so I can iterate over each with new style
    green, amber, red = classify_by_time(licenses)

    context = {'green':green, 'amber':amber, 'red':red}
    return render(request, 'expired.html', context)