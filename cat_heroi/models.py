from django.db import models


# Create your models here.

class Categoria(models.Model):
    nome = models.Chafield(
        max_lenght=255,
        verbose_name='Nome Categoria'
    )