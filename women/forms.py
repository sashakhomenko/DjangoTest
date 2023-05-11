from django import forms
from .models import *


class AddWomenForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = '__all__'