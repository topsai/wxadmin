#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/3/3

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from wx_user_ui.models import BigImage, ShopName, Commodity, CommodityInfo, BigPic


class BigImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BigImage
        fields = '__all__'


class ShopNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShopName
        fields = '__all__'


class CommoditySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commodity
        fields = ('id', 'name', 'min_price', 'max_price', 'pic', 'commodity_info')


class CommodityInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommodityInfo
        fields = ('id', 'com', 'big_pic')


class BigPicInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BigPic
        fields = ('pic_path',)
