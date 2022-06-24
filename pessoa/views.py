from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pessoas
from .forms import PessoaForm


class ListaPessoaView(ListView):
  model = Pessoas
  queryset = Pessoas.objects.all().order_by('nome_completo')

  def get_queryset(self):
    queryset = super().get_queryset()
    filtro_nome = self.request.GET.get('nome') or None

    if filtro_nome:
      queryset = queryset.filter(nome_completo__contains=filtro_nome)

    return queryset


class PessoaCreateView(CreateView):
  model = Pessoas
  form_class = PessoaForm
  success_url = '/pessoas/'

class PessoaUpdateView(UpdateView):
  model = Pessoas
  form_class = PessoaForm
  success_url = '/pessoas/'

class PessoaDeleteView(DeleteView):
  model = Pessoas
  success_url = '/pessoas/'