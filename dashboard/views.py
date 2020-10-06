from django.shortcuts import render, get_object_or_404

from .models import License, Soldier, Machine

from .helper_funcs import *




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
    unique_names = get_unique_licenses()
    print("TESTTT ==================================================================")
    print(unique_names)
    context = {'unique_names':unique_names}
    return render(request, 'assign_licenses.html', context)


def license_details(request):
    context = {}
    return render(request, 'license_details.html', context)


