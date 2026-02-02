from django import forms
from .models import NGOActivity

class NGOActivityForm(forms.ModelForm):
    class Meta:
        model = NGOActivity
        fields = [
            'ngo_name', 
            'description', 
            'location', 
            'service_type', 
            'date_time', 
            'max_employees', 
            'cut_off_date'
        ]

        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'cut_off_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }