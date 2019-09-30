from rest_framework import serializers
from .models import Universo


class UniversoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universo
        fields = ('id', 'nome')


class UniversoLightSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField()
