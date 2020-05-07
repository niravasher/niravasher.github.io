from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)


    class Meta:
        model = Project
        fields = '__all__'


