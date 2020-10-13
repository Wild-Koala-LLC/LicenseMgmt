from .models import License, Soldier, Machine

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
    green = []
    amber = []
    red =[]