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
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = HabilidadeSerializer


class HabilidadeList(views.APIView):
    def get(self, request):
        habilidades = Habilidade.objects.all()
        serializer = HabilidadeLightSerializer(habilidades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = HabilidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HabilidadeDetails(views.APIView):
    def get_object(self, id):
        try:
            return Habilidade.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id):
        habilidade = self.get_object(id)
        serializer = HabilidadeSerializer(habilidade)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        habilidade = self.get_object(id)
        serializer = HabilidadeSerializer(habilidade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)