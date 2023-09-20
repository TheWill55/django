from django import forms
from .models import NumeroEscolhido

class EscolhaNumeroForm(forms.ModelForm):
    class Meta:
        model = NumeroEscolhido
        fields = ['numero']
        