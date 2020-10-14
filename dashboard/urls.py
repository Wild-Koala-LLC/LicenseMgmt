from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assigned', views.assigned, name='assigned'),
    path('assign_licenses', views.assign_licenses, name='assign_licenses'),
    re_path(r'license_details/(?P<wanted_license>[\w|\W]+)', views.license_details, name='license_details'), 
    path('expiring', views.expiring, name='expiring'),  
    path('csv_view', views.csv_view, name='csv_view'),
    path('delete/<int:license_id>', views.delete, name='delete'),
]