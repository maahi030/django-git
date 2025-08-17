from django import forms
from .models import Projects,ProjectAttendance

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['project_name','project_type','start_year','end_year','start_month','end_month','is_active']
        widgets = {
            'project_name': forms.TextInput(attrs={'class':'form-control'}),
            'project_type': forms.Select(attrs={'class': 'form-select'}),
            'start_year': forms.NumberInput(attrs={'class':'form-control'}),
            'end_year': forms.NumberInput(attrs={'class':'form-control'}),
            'start_month': forms.NumberInput(attrs={'class':'form-control'}),
            'end_month': forms.NumberInput(attrs={'class':'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }

class ProjectAttendanceForm(forms.ModelForm):
    class Meta:
        model = ProjectAttendance
        fields = ['year','month','project_profile','resources','poc','present_days','billable_days','non_billable_days','billable_hours','non_billable_hours','extra_hours']
        widgets = {
            'year': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'month': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'project_profile': forms.Select(attrs={'class': 'form-select'}),
            'resources': forms.Select(attrs={'class': 'form-select'}),
            'poc': forms.Select(attrs={'class': 'form-select'}),
            'present_days': forms.NumberInput(attrs={'class':'form-control'}),
            'billable_days': forms.NumberInput(attrs={'class':'form-control'}),
            'non_billable_days': forms.NumberInput(attrs={'class':'form-control'}),
            'billable_hours': forms.NumberInput(attrs={'class':'form-control'}),
            'non_billable_hours': forms.NumberInput(attrs={'class':'form-control'}),
            'extra_hours': forms.NumberInput(attrs={'class':'form-control'}),
        }