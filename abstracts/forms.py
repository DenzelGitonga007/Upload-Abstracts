from django import forms
from .models import Abstract

class AbstractForm(forms.ModelForm):
    class Meta:
        model = Abstract
        fields = ['title', 'description', 'file']

    def __init__(self, *args, **kwargs):
        super(AbstractForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'accept': 'application/pdf, application/msword, text/plain'})
