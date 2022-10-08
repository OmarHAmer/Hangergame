from django import forms
from .models import Parties


class PartiesForm(forms.ModelForm):
    class Meta:
        model = Parties
        fields = ['party_number','party_name','telephone','address','party_type']
