from django.shortcuts import render, get_object_or_404

from .models import License, Soldier, Machine


# User Chart.js to make a pie chart with % of a type of license used vs. Not used
def index(request):
    # total number of licenses
    total_cool_licenses = License.objects.filter(name="Cool License").count()

    # total number of licenses who's value for "on_machine" is None
    not_in_use = License.objects.filter(
        name="Cool License",
        on_machine = None,
    ).count()

    in_use = total_cool_licenses - not_in_use

    labels = ['Available', 'In Use']
    data = [not_in_use, in_use]
    context = {'labels':labels, 'data':data}
    return render(request, 'pie_chart.html', context)

def assigned(request):
    soldier_list = Soldier.objects.order_by('name')
    machine_list = Machine.objects.order_by('serial_number')
    license_list = License.objects.order_by('-pub_date')
    context = {'soldier_list':soldier_list, 'machine_list':machine_list, 'license_list':license_list}
    return render(request, 'assigned.html', context)





