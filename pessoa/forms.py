from dataclasses import field
from django import forms
from .models import Pessoas


class PessoaForm(forms.ModelForm):
  data_nascimento = forms.DateField(
    widget=forms.TextInput(
      attrs={"type": "date"}
    )
  )

  class Meta:
    model = Pessoas
    fields = ['nome_completo', 'data_nascimento', 'ativo']