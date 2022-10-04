from django import forms
from .models import Parties


class PartiesForm(forms.ModelForm):
    class Meta:
        model = Parties
        fields = '__all__'