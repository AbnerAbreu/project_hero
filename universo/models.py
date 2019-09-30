from django.db import models

# Create your models here.
class Universo(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name='Nome Universo'
    )

    def __init__(self):
        return self.nome