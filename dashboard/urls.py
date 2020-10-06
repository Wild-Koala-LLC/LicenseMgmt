from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assigned', views.assigned, name='assigned'),
    path('assign_licenses', views.assign_licenses, name='assign_licenses'),
    path('license_details', views.license_details, name='license_details'),
    path('form_test', views.form_test, name='form_test'),
]