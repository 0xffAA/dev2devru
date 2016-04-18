from django import forms
from .models import Visitor, Event


class NewVisitorForm(forms.ModelForm):
    event = forms.ModelChoiceField(
        queryset=Event.objects.all(),
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Visitor
        fields = '__all__'
