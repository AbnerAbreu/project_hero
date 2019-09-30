from rest_framework import serializers

from cat_heroi.models import Categoria
from heroi.models import Heroi
from universo.models import Universo


class UniversoDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(max_length=255)


class HabilidadeDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(max_length=255)


class CategoriaDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(max_length=255)


class HeroiSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255)
    idade = serializers.IntegerField()
    universo = UniversoDTOSerializer()
    habilidades = HabilidadeDTOSerializer()
    categoria = CategoriaDTOSerializer()


    def create(self, validated_data):
        universo_data = validated_data.pop('universo')
        universo = Universo.objects.get(id=universo_data[id])
        categoria_data = validated_data.pop('categoria')
        categoria = Categoria.objects.get(id=categoria_data[id])
        heroi = Heroi.objects.create(categoria=categoria,universo=universo, **validated_data)
        return heroi


    def update(self, instance, validated_data):
         instance.nome = validated_data.get('nome')
         instance.idade = validated_data.get('idade')
         instance.save()
         return instance



