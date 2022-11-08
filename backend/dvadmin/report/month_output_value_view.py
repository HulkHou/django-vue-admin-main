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


class ReportOutputvalueSerializer(CustomModelSerializer):
    """
    月度产值报表-序列化器
    """

    class Meta:
        model = ReportOutputvalue
        fields = "__all__"
        read_only_fields = ["id"]


class ReportMonthOutputvalueViewSet(CustomModelViewSet):
    """
    月度产值报表接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = ReportOutputvalue.objects.all()
    serializer_class = ReportOutputvalueSerializer


class GetReportMonthOutputvalueView(CustomModelViewSet):
    permission_classes = []
    queryset = ReportOutputvalue.objects.all()
    serializer_class = ReportOutputvalueSerializer

    def get_report_month_outputvalue(self, request, *args, **kwargs):
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

        for index in range(len(output_value_list)):
            a = output_value_list[index]
            labels.append(a.get('month') + '月')
            output_value_lowest.append(a.get('output_value_lowest'))
            output_value_target.append(a.get('output_value_target'))
            output_value_actual.append(a.get('output_value_actual'))

        x = np.arange(len(labels))  # the label locations
        width = 0.25  # the width of the bars

        x2 = [p + width for p in x]
        x3 = [p + 2 * width for p in x]

        fig, ax = plt.subplots()
        rects1 = ax.bar(x, output_value_lowest, width, label='月度产值-保底计划')
        rects2 = ax.bar(x2, output_value_target, width, label='月度产值-力争计划')
        rects3 = ax.bar(x3, output_value_actual, width, label='月度产值-实际')

        # Y轴显示百分比
        ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=100, decimals=2))

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_xlabel('月份')
        ax.set_ylabel('产值')
        ax.set_title('马东铁' + year + '年月度产值与实际直方图和曲线')
        ax.set_xticks(x, labels)
        ax.legend(loc='upper left')

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)
        ax.bar_label(rects3, padding=3)

        ax2 = ax.twinx()

        labels = []
        output_value_lowest = []
        output_value_target = []
        output_value_actual = []

        output_value_lowest_num = 0
        output_value_target_num = 0
        output_value_actual_num = 0

        for index in range(len(output_value_list)):
            a = output_value_list[index]
            labels.append(a.get('month') + '月')
            output_value_lowest_num = output_value_lowest_num + a.get('output_value_lowest')
            output_value_target_num = output_value_target_num + a.get('output_value_target')
            output_value_actual_num = output_value_actual_num + a.get('output_value_actual')

            output_value_lowest.append(round(output_value_lowest_num, 2))
            output_value_target.append(round(output_value_target_num, 2))
            output_value_actual.append(round(output_value_actual_num, 2))

        ax2.plot(labels, output_value_lowest, label='累计产值-保底计划', color='c')
        ax2.plot(labels, output_value_target, label='累计产值-力争计划', color='m')
        ax2.plot(labels, output_value_actual, label='累计产值-实际', color='r')

        ax2.legend(loc='upper right')

        # Y轴显示百分比
        ax2.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=100, decimals=2))

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

    def get_report_month_outputvalue_list(self, request, *args, **kwargs):
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
                output_value_last_year=Sum('output_value_last_year'),
                section_name=Count('section_name')).order_by(
                'month')

        serializer = self.get_serializer(queryset, many=True, request=request)

        output_value_list = serializer.data

        labels = []
        output_value_lowest = []
        output_value_target = []
        output_value_actual = []
        output_value_last_year = []
        data_list = []

        for index in range(len(output_value_list)):
            a = output_value_list[index]
            labels.append(a.get('month'))
            output_value_lowest.append(round(a.get('output_value_lowest'), 2))
            output_value_target.append(round(a.get('output_value_target'), 2))
            output_value_actual.append(round(a.get('output_value_actual'), 2))
            output_value_last_year.append(round(a.get('output_value_last_year'), 2))

        output_value_lowest_sum = []
        output_value_target_sum = []
        output_value_actual_sum = []

        output_value_lowest_num = 0
        output_value_target_num = 0
        output_value_actual_num = 0

        for index in range(len(output_value_list)):
            a = output_value_list[index]
            output_value_lowest_num = output_value_lowest_num + a.get('output_value_lowest')
            output_value_target_num = output_value_target_num + a.get('output_value_target')
            output_value_actual_num = output_value_actual_num + a.get('output_value_actual')

            output_value_lowest_sum.append(round(output_value_lowest_num, 2))
            output_value_target_sum.append(round(output_value_target_num, 2))
            if not (a.get('output_value_actual') == 0 and output_value_actual_num != 0):
                output_value_actual_sum.append(round(output_value_actual_num, 2))

        data_list.append(labels)
        data_list.append(output_value_lowest)
        data_list.append(output_value_target)
        data_list.append(output_value_actual)
        # data_list.append(output_value_lowest_sum)
        data_list.append(output_value_last_year)
        data_list.append(output_value_target_sum)
        data_list.append(output_value_actual_sum)

        return DetailResponse(data=data_list)
