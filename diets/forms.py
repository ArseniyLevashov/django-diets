from django import forms
from .models import Diet, Result


class DietForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = ['name', 'description', 'start_date', 'start_weight']


class ResultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = ['diet_id', 'current_date', 'current_weight']
        widgets = {'diet_id': forms.HiddenInput()}
