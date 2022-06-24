from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ContatoForm, PessoaForm
from .models import Contato, Pessoas


class ListaPessoaView(ListView):
    model = Pessoas
    queryset = Pessoas.objects.all().order_by('nome_completo')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(usuario=self.request.user)
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)

        return queryset


class PessoaCreateView(CreateView):
    model = Pessoas
    form_class = PessoaForm
    success_url = '/pessoas/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class PessoaUpdateView(UpdateView):
    model = Pessoas
    form_class = PessoaForm
    success_url = '/pessoas/'


class PessoaDeleteView(DeleteView):
    model = Pessoas
    success_url = '/pessoas/'


def contatos(request, pk_pessoa):
    contatos = Contato.objects.filter(pessoa=pk_pessoa)
    return render(request, 'contato/contato_list.html',
                  {'contatos': contatos, 'pk_pessoa': pk_pessoa})


def contato_novo(request, pk_pessoa):
    form = ContatoForm()
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save(commit=False)
            contato.pessoa_id = pk_pessoa
            contato.save()
            return redirect(reverse('pessoa.contatos', args=[pk_pessoa]))
    return render(request, 'contato/contato_form.html', {'form': form})


def contato_editar(request, pk_pessoa, pk):
    contato = get_object_or_404(Contato, pk=pk)
    form = ContatoForm(instance=contato)
    if request.method == "POST":
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            contato.save()
            return redirect(reverse('pessoa.contatos', args=[pk_pessoa]))
    return render(request, 'contato/contato_form.html', {'form': form})


def contato_remover(request, pk_pessoa, pk):
    contato = get_object_or_404(Contato, pk=pk)
    contato.delete()
    return redirect(reverse('pessoa.contatos', args=[pk_pessoa]))
