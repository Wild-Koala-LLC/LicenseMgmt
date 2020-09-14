from django.shortcuts import render, get_object_or_404

from .models import License, Soldier, Machine

def index(request):
	soldier_list = Soldier.objects.order_by('name')
	machine_list = Machine.objects.order_by('serial_number')
	license_list = License.objects.order_by('-pub_date')
	context = {'soldier_list':soldier_list, 'machine_list':machine_list, 'license_list':license_list}
	return render(request, 'dashboard.html', context)

def test(request):
	soldier_list = Soldier.objects.order_by('name')
	machine_list = Machine.objects.order_by('serial_number')
	license_list = License.objects.order_by('-pub_date')
	context = {'soldier_list':soldier_list, 'machine_list':machine_list, 'license_list':license_list}
	return render(request, 'dashboard2.html', context)


'''
def detail(request, question_id):
	license = get_object_or_404(License, pk=license_id)
	return render(request, 'license.html', {'license':license})
'''