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
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategoriaSerializer


class CategoriaList(views.APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaLightSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaDetails(views.APIView):
    def get_object(self, id):
        try:
            return Categoria.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id):
        categoria = self.get_object(id)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        categoria = self.get_object(id)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer .is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)