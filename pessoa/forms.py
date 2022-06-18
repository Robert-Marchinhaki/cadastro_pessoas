from dataclasses import field
from django import forms
from .models import Pessoas


class PessoaForm(forms.ModelForm):
  class Meta:
    model = Pessoas
    fields = ['nome_completo', 'data_nascimento', 'ativo']