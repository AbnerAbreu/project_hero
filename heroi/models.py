from django.db import models


# Create your models here.
from cat_heroi.models import Categoria
from habilidade.models import Habilidade
from universo.models import Universo


class Heroi(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name='nome'
    )
    idade = models.IntegerField(
        verbose_name='idade'
    )
    heroi_uni = models.ForeignKey(
        Universo,
        on_delete=models.CASCADE,
        related_name='heroi_uni'
    )
    heroi_hab = models.ManyToManyField(
        Habilidade,
        # on_delete=models.CASCADE,
        related_name='heroi_hab'
    )
    heroi_cat = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='heroi_cat'
    )