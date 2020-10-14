from import_export import resources
from .models import License

class LicenseResource(resources.ModelResource):
    class Meta:
        model = License