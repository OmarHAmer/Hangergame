from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Items



class FormItems(forms.ModelForm):
    class Meta:
        model=Items
        fields=['code','description','item_type','category','order_flag','batch_flag','complete_flag']
