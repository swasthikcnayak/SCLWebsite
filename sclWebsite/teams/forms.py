from django import forms

from .models import Teams


class TeamUpdateForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = ['points', 'cookies']
