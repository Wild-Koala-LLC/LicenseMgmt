from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pie_chart', views.pie_chart, name='pie_chart'),
    path('everything', views.everything, name='everything'),
    path('assign_licenses', views.assign_licenses, name='assign_licenses'),
    path('remaining', views.remaining, name='remaining'),
]