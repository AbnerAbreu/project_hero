from rest_framework import serializers
from .models import Universo


class UniversoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255)

    def create(self, validated_data):
        universo = Universo.objects.create(**validated_data)
        return universo

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.save()
        return instance


class UniversoLightSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField()
