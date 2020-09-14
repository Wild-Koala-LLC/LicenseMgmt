from django.shortcuts import render, get_object_or_404

from .models import License

def index(request):
	license_list = License.objects.order_by('-pub_date')
	context = {'license_list':license_list}
	return render(request, 'dashboard.html', context)

def detail(request, question_id):
	license = get_object_or_404(License, pk=license_id)
	return render(request, 'license.html', {'license':license})