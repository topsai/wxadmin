from django.shortcuts import render, HttpResponse

# Create your views here.
from wx_user_ui.models import BigImage, UserUI, ModuleType, ShopName, Commodity, CommodityInfo
from wx_user_ui.serializers import BigImageSerializer, ShopNameSerializer, CommoditySerializer, CommodityInfoSerializer
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


class CommodityInfoVIewSet(viewsets.ModelViewSet):
    queryset = CommodityInfo.objects.all()
    serializer_class = CommodityInfoSerializer


from wxadmin.settings import wxloginapi
import requests


def login(data):
    code = data.GET.get("code")
    r = requests.post(wxloginapi, data={
        'appid': 'wxb11c8642b5007e82',
        'secret': '41035b5dc2c09eb18123ddd0c90d3be3',
        'js_code': code,
        'grant_type': 'authorization_code',
    }
                      )
    print(r.json())
    return HttpResponse(r.text)
# appid	string		是	小程序 appId
# secret	string		是	小程序 appSecret
# js_code	string		是	登录时获取的 code
# grant_type	string		是	授权类型，此处只需填写 authorization_code
