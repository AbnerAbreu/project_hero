from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from universo.models import Universo
from universo.serializers import UniversoSerializer, UniversoLightSerializer


class UniversoViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['Nome Universo']
    queryset = Universo.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = UniversoSerializer
