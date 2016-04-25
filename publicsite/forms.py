from django import forms
from .models import Visitor, Event


class NewVisitorForm(forms.ModelForm):
    event = forms.ModelChoiceField(
        queryset=Event.objects.all(),
        widget=forms.HiddenInput()
    )
    position = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'работаешь кем?'})
    )
    company = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'работаешь где?'})
    )

    class Meta:
        model = Visitor
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'em@il'}),
            'name': forms.TextInput(attrs={'placeholder': 'имя'}),
        }
