from django import forms
from .models import Resource,ResourceAttendace

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['resource_name','join_date','leave_date','is_active']
        widgets = {
            'resource_name': forms.TextInput(attrs={'class':'form-control'}),
            'join_date': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'leave_date': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }

class ResourceAttendanceForm(forms.ModelForm):
    class Meta:
        model = ResourceAttendace
        fields = ['year','month','working_days','present_day','present_hours']
        widgets = {
            'year': forms.NumberInput(attrs={'class':'form-control'}),
            'month': forms.NumberInput(attrs={'class':'form-control'}),
            'working_days': forms.NumberInput(attrs={'class':'form-control'}),
            'present_day': forms.NumberInput(attrs={'class':'form-control'}),
            'present_hours': forms.NumberInput(attrs={'class':'form-control'})
        }