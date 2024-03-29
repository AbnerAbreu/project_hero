from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from cat_heroi.models import Categoria
from cat_heroi.serializers import CategoriaSerializer, CategoriaLightSerializer
from rest_framework.response import Response


class CategoriaViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['Nome Categoria']
    queryset = Categoria.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = CategoriaSerializer
