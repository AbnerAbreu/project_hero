from rest_framework import serializers
from heroi.models import Heroi


class HeroiSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255)
    idade = serializers.IntegerField()

    def create(self, validated_data):
        heroi = Heroi.objects.create(**validated_data)
        return heroi

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('idade')
        instance.save()
        return instance


class HeroiLightSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField()
    idade = serializers.IntegerField()
