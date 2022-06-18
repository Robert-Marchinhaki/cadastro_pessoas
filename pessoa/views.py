from django.shortcuts import render
from django.views.generic import ListView
from .models import Pessoas


class ListaPessoaView(ListView):
  model = Pessoas
  queryset = Pessoas.objects.all().order_by('nome_completo')