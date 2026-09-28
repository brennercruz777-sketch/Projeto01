from django import forms
from .models import Vaga

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo_vaga', 'empresa', 'modalidade', 'salario', 'requisitos', 'ativa']
        widgets = {
            'titulo_vaga': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'modalidade': forms.Select(attrs={'class': 'form-select'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'requisitos': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'ativa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }