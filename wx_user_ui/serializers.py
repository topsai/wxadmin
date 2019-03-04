#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/3/3

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from wx_user_ui.models import BigImage


class BigImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BigImage
        fields = '__all__'
