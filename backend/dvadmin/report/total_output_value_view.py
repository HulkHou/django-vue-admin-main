import base64
import io

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from django.db.models import Count, Sum

from django.shortcuts import render

from dvadmin.system.models import ReportOutputvalue
from dvadmin.utils.viewset import CustomModelViewSet
from dvadmin.utils.serializers import CustomModelSerializer
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from dvadmin.utils.json_response import DetailResponse, SuccessResponse, ErrorResponse

matplotlib.use('Agg')


class ReportTotalOutputvalueSerializer(CustomModelSerializer):
    """
    月度产值报表-序列化器
    """

    class Meta:
        model = ReportOutputvalue
        fields = "__all__"
        read_only_fields = ["id"]


class ReportOutputvalueViewSet(CustomModelViewSet):
    """
    月度产值报表接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = ReportOutputvalue.objects.all()
    serializer_class = ReportTotalOutputvalueSerializer


class GetReportTotalOutputvalueView(CustomModelViewSet):
    queryset = ReportOutputvalue.objects.all()
    serializer_class = ReportTotalOutputvalueSerializer

    def get_report_total_outputvalue(self, request, *args, **kwargs):
        section = self.request.query_params.get('section')
        year = self.request.query_params.get('year')

        queryset = self.filter_queryset(self.get_queryset())

        if section:
            queryset = queryset.filter(section_name=section)
        else:
            queryset = queryset.values('year', 'month').annotate(
                output_value_lowest=Sum('output_value_lowest'),
                output_value_target=Sum('output_value_target'),
                output_value_actual=Sum('output_value_actual'),
                section_name=Count('section_name')).order_by(
                'month')

        serializer = self.get_serializer(queryset, many=True, request=request)

        output_value_list = serializer.data

        context = {}
        img = io.BytesIO()

        plt.rcParams["font.family"] = "sans-serif"
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        # 设置图表尺寸
        plt.rcParams['figure.figsize'] = (16.0, 8.0)

        labels = []
        output_value_lowest = []
        output_value_target = []
        output_value_actual = []

        output_value_lowest_num = 0
        output_value_target_num = 0
        output_value_actual_num = 0

        for index in range(len(output_value_list)):
            a = output_value_list[index]
            labels.append(a.pop('month') + '月')
            output_value_lowest_num = output_value_lowest_num + a.pop('output_value_lowest')
            output_value_target_num = output_value_target_num + a.pop('output_value_target')
            output_value_actual_num = output_value_actual_num + a.pop('output_value_actual')

            output_value_lowest.append(round(output_value_lowest_num, 2))
            output_value_target.append(round(output_value_target_num, 2))
            output_value_actual.append(round(output_value_actual_num, 2))

        fig, ax = plt.subplots()
        ax.plot(labels, output_value_lowest, label='累计产值-保底计划')
        ax.plot(labels, output_value_target, label='累计产值-力争计划')
        ax.plot(labels, output_value_actual, label='累计产值-实际')

        # Y轴显示百分比
        ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=100, decimals=2))

        ax.set_xlabel('月份')
        ax.set_ylabel('产值')
        ax.set_title('马东铁' + year + '年累计产值与实际直方图和曲线')
        ax.legend()  # Add a legend.

        # 给图像添加注释，并设置样式
        for a, b in zip(labels, output_value_lowest):
            plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

        for a, b in zip(labels, output_value_target):
            plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

        for a, b in zip(labels, output_value_actual):
            plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

        fig.tight_layout()

        plt.savefig(img, format='png')
        img.seek(0)

        plot_url = base64.b64encode(img.getvalue()).decode()

        context["plot_url"] = plot_url

        return DetailResponse(data=context)
