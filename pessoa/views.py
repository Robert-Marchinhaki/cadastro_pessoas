from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Pessoas
from .forms import PessoaForm


class ListaPessoaView(ListView):
  model = Pessoas
  queryset = Pessoas.objects.all().order_by('nome_completo')


class PessoaCreateView(CreateView):
  model = Pessoas
  form_class = PessoaForm
  success_url = '/pessoas/'