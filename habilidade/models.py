from django.db import models

# Create your models here.

class Habilidade(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name='habilidade'
    )
