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
