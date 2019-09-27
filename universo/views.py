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
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = UniversoSerializer


class UniversoList(views.APIView):
    def get(self, request):
        universos = Universo.objects.all()
        serializer = UniversoLightSerializer(universos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UniversoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UniversoDetails(views.APIView):
    def get_object(self, id):
        try:
            return Universo.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id):
        universo = self.get_object(id)
        serializer = UniversoSerializer(universo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        universo = self.get_object(id)
        serializer = UniversoSerializer(universo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)