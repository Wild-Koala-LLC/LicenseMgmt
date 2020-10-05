from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('remaining', views.remaining, name='remaining'),
    path('assign_licenses', views.assign_licenses, name='assign_licenses'),
]