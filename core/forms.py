from django import forms
from core.models import Piloto


class PilotoModelForm(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = ['imagem', 'nome', 'idade', 'altura']
