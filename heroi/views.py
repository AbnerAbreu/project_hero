from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from heroi.models import Heroi
from heroi.serializers import HeroiSerializer, HeroiLightSerializer


class HeroiViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome', '=idade']
    queryset = Heroi.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = HeroiSerializer


class HeroiList(views.APIView):
    def get(self, request):
        herois = Heroi.objects.all()
        serializer = HeroiLightSerializer(herois, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = HeroiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeroiDetails(views.APIView):
    def get_object(self, id):
        try:
            return Heroi.objects.get(id=id)
        except:
            raise Http404
    def get(self, request, id):
        heroi = self.get_object(id)
        serializer = HeroiSerializer(heroi)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        heroi = self.get_object(id)
        serializer = HeroiSerializer(heroi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)