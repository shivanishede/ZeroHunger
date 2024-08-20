from django import forms
from .models import DonarInfo

class DonarInfoForm(forms.ModelForm):
    class Meta:
        model = DonarInfo
        fields = '__all__'
