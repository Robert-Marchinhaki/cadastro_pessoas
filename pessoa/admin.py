from django.contrib import admin
from .models import Contato, Pessoas

# Register your models here.


@admin.action(description="Ativar todas as pessoas")
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativo=True)


@admin.action(description='Desativar todas as pessoas')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativo=False)


class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'data_nascimento',
        'ativo'
    ]
    list_filter = [
        'ativo',
        'data_nascimento'
    ]
    search_fields = [
        'nome_completo'
    ]
    actions = [
        ativar_todos,
        desativar_todos
    ]


admin.site.register(Pessoas, PessoaAdmin)
admin.site.register(Contato)
