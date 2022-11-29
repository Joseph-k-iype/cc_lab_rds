from django import forms
from .models import Covid_details

class CovidForm(forms.ModelForm):
    class Meta:
        model = Covid_details
        fields = "__all__"
        widgets = {
            'state_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_record': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'No_of_samples': forms.NumberInput(attrs={'class': 'form-control'}),
            'no_of_deaths': forms.NumberInput(attrs={'class': 'form-control'}),
            'no_of_positive': forms.NumberInput(attrs={'class': 'form-control'}),
            'no_of_negative': forms.NumberInput(attrs={'class': 'form-control'}),
            'no_of_discharged': forms.NumberInput(attrs={'class': 'form-control'}),
        }
