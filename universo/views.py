
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from universo.models import Universo
from universo.serializers import UniversoSerializer


class UniversoViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    # search_fields = ['Nome Universo']
    queryset = Universo.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = UniversoSerializer
