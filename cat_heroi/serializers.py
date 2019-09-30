from rest_framework import serializers
from .models import Categoria


class CategoriaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255)

    def create(self, validated_data):
        categoria = Categoria.objects.create(**validated_data)
        return categoria

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.save()
        return instance


class CategoriaLightSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField()
