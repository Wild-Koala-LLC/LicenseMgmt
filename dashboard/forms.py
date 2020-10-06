from django import forms
from .models import License

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class TestForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)

class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ['name', 'key', 'start_date', 'end_date', 'on_machine']