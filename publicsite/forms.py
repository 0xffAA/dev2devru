from django import forms
from .models import Visitor, Event


class NewVisitorForm(forms.ModelForm):
    event = forms.ModelChoiceField(
        queryset=Event.objects.all(),
        widget=forms.HiddenInput()
    )
    position = forms.CharField(
        required=False
    )
    company = forms.CharField(
        required=False
    )

    class Meta:
        model = Visitor
        exclude = ['registered_at']