"""project_hero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from cat_heroi.views import CategoriaViewSet, CategoriaList, CategoriaDetails
from universo.views import UniversoViewSet, UniversoList, UniversoDetails
from heroi.views import HeroiViewSet, HeroiList, HeroiDetails
from habilidade.views import HabilidadeViewSet, HabilidadeList, HabilidadeDetails



router = routers.DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
router.register(r'universo', UniversoViewSet)
router.register(r'herois', HeroiViewSet)
router.register(r'habilidades', HabilidadeViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('herois/<int:id>', HeroiDetails.as_view()),
    path('herois', HeroiList.as_view()),
    path('',include(router.urls)),
    path('token', obtain_auth_token),
    
]
