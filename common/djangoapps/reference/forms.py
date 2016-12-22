from django import forms
from .models import Reference


class ReferenceForm(forms.ModelForm):

    class Meta:
        model = Reference
        fields = [
            'reference_name', 'reference_type', 'reference_link',
            'reference_description', 'reference_status'
            ]


