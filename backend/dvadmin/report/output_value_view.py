# -*- coding: utf-8 -*-

"""
@author: Hulk
@Remark: 产值数据管理
"""
from rest_framework import serializers

from dvadmin.system.models import ReportOutputvalue
from dvadmin.utils.json_response import DetailResponse, SuccessResponse
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class OutputvalueSerializer(CustomModelSerializer):
    """
    产值数据管理-序列化器
    """

    class Meta:
        model = ReportOutputvalue
        fields = '__all__'
        read_only_fields = ["id"]


class OutputvalueCreateUpdateSerializer(CustomModelSerializer):
    """
    产值数据管理 创建/更新时的列化器
    """

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.dept_belong_id = instance.id
        instance.save()
        return instance

    class Meta:
        model = ReportOutputvalue
        fields = '__all__'


class OutputvalueViewSet(CustomModelViewSet):
    """
    产值数据管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    permission_classes = []
    queryset = ReportOutputvalue.objects.all()
    serializer_class = OutputvalueSerializer
    create_serializer_class = OutputvalueCreateUpdateSerializer
    update_serializer_class = OutputvalueCreateUpdateSerializer
    # filter_fields = ['section', 'year']
    search_fields = []

    # def list(self, request, *args, **kwargs):
    #     section = self.request.query_params.get('section')
    #     year = self.request.query_params.get('year')
    #
    #     queryset = self.filter_queryset(self.get_queryset())
    #     if section:
    #         queryset = queryset.filter(section_name=section)
    #
    #     serializer = self.get_serializer(queryset, many=True, request=request)
    #     return SuccessResponse(data=serializer.data, msg="获取成功")
