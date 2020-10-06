from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import License, Soldier, Machine

from .helper_funcs import *

from .forms import NameForm, TestForm, LicenseForm




# User Chart.js to make a pie chart with % of a type of license used vs. Not used
def index(request):
    
    unique = get_unique_licenses()
    license_dict = get_used_and_unused(unique) 
    print(license_dict) 
    # I'm getting back a dictionary in this format
    # str(name) : list[int available, int used]
    

    labels = ['Available', 'In Use']
    #data = results['Cool License'] # when this is passed the current dash works

    context = {'labels':labels, 'license_dict':license_dict}
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
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("GOOD FORM CAME THRU======================================================")
            return HttpResponseRedirect('/license_details')

    # if a GET (or any other method) we'll create a blank form
    else:
        unique_names = get_unique_licenses()
        current_user = "Your Name Here!"
        form = NameForm()
        context = {'unique_names':unique_names, 'current_user':current_user, 'form':form}
        return render(request, 'assign_licenses.html', context)


def license_details(request):
    context = {}
    return render(request, 'license_details.html', context)




def form_test(request):

    if request.method == 'POST':
        form = LicenseForm(request.POST)
        if form.is_valid():
            print("GOT VALID LICENSE!==============================================")
            form.save()

    form = LicenseForm()
    context = {'form':form}
    return render(request, 'form_test.html', context)