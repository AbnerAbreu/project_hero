from django.db import models


# Create your models here.


class Heroi(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name='nome'
    )
    idade = models.IntegerField(
        verbose_name='idade'
    )
