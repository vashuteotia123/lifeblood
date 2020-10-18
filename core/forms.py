from django import forms
from .models import BloodDonor


class BloodDonorForm(forms.ModelForm):
    class Meta:
        model = BloodDonor
        fields = '__all__'
