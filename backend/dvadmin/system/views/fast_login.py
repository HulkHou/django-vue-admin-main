# -*- coding: utf-8 -*-

"""
@author: 猿小天
@contact: QQ:1638245306
@Created on: 2021/6/3 003 0:30
@Remark: 字典管理
"""
import json

from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from rest_framework import serializers
from rest_framework.views import APIView

from application import dispatch
from dvadmin.system.models import Dictionary
from dvadmin.utils.json_response import SuccessResponse
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet
from django.contrib import auth
from dvadmin.utils.json_response import DetailResponse, SuccessResponse, ErrorResponse

import jpype
import os


class FastLoginSerializer(CustomModelSerializer):
    """
    字典-序列化器
    """

    class Meta:
        model = Dictionary
        fields = "__all__"
        read_only_fields = ["id"]


class FastLoginInitSerializer(CustomModelSerializer):
    """
    初始化获取数信息(用于生成初始化json文件)
    """
    children = serializers.SerializerMethodField()

    def get_children(self, obj: Dictionary):
        data = []
        instance = Dictionary.objects.filter(parent_id=obj.id)
        if instance:
            serializer = FastLoginInitSerializer(instance=instance, many=True)
            data = serializer.data
        return data

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        children = self.initial_data.get('children')
        # 菜单表
        if children:
            for data in children:
                data['parent'] = instance.id
                filter_data = {
                    "value": data['value'],
                    "parent": data['parent']
                }
                instance_obj = Dictionary.objects.filter(**filter_data).first()
                if instance_obj and not self.initial_data.get('reset'):
                    continue
                serializer = FastLoginInitSerializer(instance_obj, data=data, request=self.request)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        return instance

    class Meta:
        model = Dictionary
        fields = ['label', 'value', 'parent', 'type', 'color', 'is_value', 'status', 'sort', 'remark', 'creator',
                  'dept_belong_id', 'children']
        read_only_fields = ["id"]
        extra_kwargs = {
            'creator': {'write_only': True},
            'dept_belong_id': {'write_only': True}
        }


class FastLoginCreateUpdateSerializer(CustomModelSerializer):
    """
    字典管理 创建/更新时的列化器
    """

    class Meta:
        model = Dictionary
        fields = '__all__'


class FastLoginViewSet(CustomModelViewSet):
    """
    字典管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Dictionary.objects.all()
    serializer_class = FastLoginSerializer
    extra_filter_backends = []
    search_fields = ['label']


class FastLoginViewSet(APIView):
    """
    获取初始化配置
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request):

        ltpa3DESKey = "JsB5e3mET2NSfddKobvASRCkiHlNWS+X69SMYWguqfs\\="
        # ltpaPassword 值 门户提供
        ltpaPassword = "123456"
        LtpaToken = ''
        LtpaToken2 = ''
        token = ''
        username = ''

        cookies = request.COOKIES
        for cookie in cookies:
            if "LtpaToken" in cookie:
                LtpaToken = cookies['LtpaToken']
            elif "LtpaToken2  " in cookie:
                LtpaToken2 = cookies['LtpaToken2']

        # 配置JVM启动环境
        jvmPath = jpype.getDefaultJVMPath()
        module_dir = os.path.dirname(__file__)

        jarpath = os.path.join(module_dir, 'ltpa-decode.jar')
        # 设置要加载的门户jar包，该包依赖commons-codec-1.4.jar，放在jre/ext文件夹中启动加载
        # jarpath = os.path.join(os.path.abspath('.'),"ltpa-decode.jar")

        # 如JVM未启动，则启动JVM
        if not jpype.isJVMStarted():
            jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=%s" % jarpath)
        # 选择要使用的java类,该类门户文档提供
        objects = jpype.JClass("com.ltpad.decode.LTPADecode")
        # 根据类解码LtpaToken，获取token。
        if LtpaToken is not None:
            token = objects.LTPATokenDecode(LtpaToken, ltpa3DESKey, ltpaPassword)
        elif LtpaToken2 is not None:
            token = objects.LTPATokenDecode(LtpaToken2, ltpa3DESKey, ltpaPassword)
        # 获取token中的uid
        if token is not None:
            uid = token.substring(token.indexOf("uid=") + 4, token.indexOf(",cn=users,DC=CHEC,DC=BJ,DC=CN"))
            print("uid")
            print(uid)
            print(type(uid))
            username = str(uid)

        data = {
            'user_name': username,
        }
        return DetailResponse(data=data)
        jpype.shutdownJVM()
