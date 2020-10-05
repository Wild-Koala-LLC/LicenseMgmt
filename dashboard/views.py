from django.shortcuts import render, get_object_or_404

from .models import License, Soldier, Machine

def index(request):
    soldier_list = Soldier.objects.order_by('name')
    machine_list = Machine.objects.order_by('serial_number')
    license_list = License.objects.order_by('-pub_date')
    context = {'soldier_list':soldier_list, 'machine_list':machine_list, 'license_list':license_list}
    return render(request, 'assigned.html', context)

def assign_licenses(request):
    soldier_list = Soldier.objects.order_by('name')
    machine_list = Machine.objects.order_by('serial_number')
    license_list = License.objects.order_by('-pub_date')
    context = {'soldier_list':soldier_list, 'machine_list':machine_list, 'license_list':license_list}
    return render(request, 'assign_licenses.html', context)

def remaining(request):
    context = {}
    return render(request, 'remaining.html', context)

def everything(request):
    soldier_list = Soldier.objects.order_by('name')
    machine_list = Machine.objects.order_by('serial_number')
    license_list = License.objects.order_by('-pub_date')
    context = {'soldier_list':soldier_list, 'machine_list':machine_list, 'license_list':license_list}
    return render(request, 'list_everything.html', context)

# User Chart.js to make a pie chart with % of a type of license used vs. Not used
def pie_chart(request):
    # total number of licenses
    total_cool_licenses = License.objects.filter(name="Cool License").count()

    # total number of licenses who's value for "on_machine" is None
    in_use = License.objects.filter(
        name="Cool License",
        on_machine = None, # hopefully it's not the string "None"
    ).count()

    not_in_use = total_cool_licenses - in_use


    labels = ['In Use', 'Available']
    data = [in_use, not_in_use]
    context = {'labels':labels, 'data':data}
    return render(request, 'pie_chart.html', context)
