from django import forms
from .models import Cronograma

class CronogramaForm(forms.ModelForm):
    class Meta:
        model = Cronograma
        fields = ['pessoa', 'titulo', 'data', 'hora_inicio', 'hora_fim']
