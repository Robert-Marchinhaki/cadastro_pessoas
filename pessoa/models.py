from django.db import models

class Pessoas(models.Model):
  nome_completo = models.CharField(max_length=256)
  data_nascimento = models.DateField(null=True)
  ativo = models.BooleanField(default=True)

  def __str__(self) -> str:
    return self.nome_completo
