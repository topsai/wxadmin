from django.shortcuts import render

# Create your views here.
from wx_user_ui.models import BigImage, UserUI, ModuleType
from wx_user_ui.serializers import BigImageSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins


class BigImageVIewSet(viewsets.ModelViewSet):
    queryset = BigImage.objects.all()
    serializer_class = BigImageSerializer
