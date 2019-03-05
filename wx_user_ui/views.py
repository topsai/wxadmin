from django.shortcuts import render

# Create your views here.
from wx_user_ui.models import BigImage, UserUI, ModuleType, ShopName, Commodity
from wx_user_ui.serializers import BigImageSerializer, ShopNameSerializer, CommoditySerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins


class BigImageVIewSet(viewsets.ModelViewSet):
    queryset = BigImage.objects.all()
    serializer_class = BigImageSerializer


class ShopNameVIewSet(viewsets.ModelViewSet):
    queryset = ShopName.objects.all()
    serializer_class = ShopNameSerializer


class CommodityVIewSet(viewsets.ModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
