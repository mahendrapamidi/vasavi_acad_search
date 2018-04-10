from django import forms

from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

DISPLAY_CHOICES = (
    (1, "Student"),
    (2, "Faculty")
)        

class Wru(forms.Form):
    display_type = forms.ChoiceField(widget=forms.RadioSelect, choices=DISPLAY_CHOICES)
