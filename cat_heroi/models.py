from django.db import models


# Create your models here.

class Categoria(models.Model):

    nome = models.CharField(
        max_length=255,
    nome = models.CharField(
        max_lenght=255,
        verbose_name='Nome Categoria'
    )