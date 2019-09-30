from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from habilidade.models import Habilidade
from habilidade.serializers import HabilidadeSerializer, HabilidadeLightSerializer


class HabilidadeViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['habilidade']
    queryset = Habilidade.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = HabilidadeSerializer


