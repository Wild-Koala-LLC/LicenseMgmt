from django.utils import timezone

from .models import License, Soldier, Machine

import datetime

def get_unique_licenses():
    # Get back all the unique license names in a list
    licenses = License.objects.values('name').distinct()
    uniq_licenses = []
    for l in licenses:
        uniq_licenses.append(l["name"])
    return uniq_licenses

def get_used_and_unused(license_names): # license_names is a list of strings.
    # Get a dictionary back 
    # name : [used, available]

    results = dict()
    for licen in license_names:
        new_list = list()

        # total number of licenses with this name
        total_num = License.objects.filter(name=licen).count()

        # total number of licenses with this name, who's value for "on_machine" is None
        not_in_use = License.objects.filter(
        name=licen,
        on_machine = None,
        ).count()

        new_list.append(not_in_use)
        
        used = total_num - not_in_use
        new_list.append(used)
        
        results[licen] = new_list
    return results


def classify_by_time(licenses):
    """ takes an ordered querySet and returns a tuple with 3 lists for the licenses in each category: green, amber, red """
    green = []
    amber = []
    red =[]

    current_date_and_time = timezone.now()

    days_ahead = 120
    hours_added = datetime.timedelta(hours = days_ahead*24)
    green_time = current_date_and_time + hours_added

    days_ahead = 60
    hours_added = datetime.timedelta(hours = days_ahead*24)
    amber_time = current_date_and_time + hours_added

    for license in licenses:
        if license.end_date >= green_time:
            green.append(license)
        elif license.end_date >= amber_time:
            amber.append(license)
        else:
            red.append(license)
        
        
    return (green, amber, red)


def get_row(obj):
    row = []
    for field in model_fields:
        if type(field) == models.ForeignKey:
            val = getattr(obj, field.name)
            if val:
                val = val.__unicode__()
        elif type(field) == models.ManyToManyField:
            val = u', '.join([item.__unicode__() for item in getattr(obj, field.name).all()])
        elif field.choices:
            val = getattr(obj, 'get_%s_display'%field.name)()
        else:
            val = getattr(obj, field.name)
        row.append(unicode(val).encode("utf-8"))
    return row