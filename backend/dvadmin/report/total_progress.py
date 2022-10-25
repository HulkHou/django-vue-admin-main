from django.db.models import Count, Sum
from dvadmin.system.models import ReportTotalProgress
from dvadmin.utils.viewset import CustomModelViewSet
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.json_response import DetailResponse, SuccessResponse, ErrorResponse


class ReportTotalProgressSerializer(CustomModelSerializer):
    """
    工期进度报表-序列化器
    """

    class Meta:
        model = ReportTotalProgress
        fields = "__all__"
        read_only_fields = ["id"]


class ReportTotalProgressViewSet(CustomModelViewSet):
    """
    工期进度报表接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = ReportTotalProgress.objects.all()
    serializer_class = ReportTotalProgressSerializer


class GetReportTotalProgressView(CustomModelViewSet):
    queryset = ReportTotalProgress.objects.all()
    serializer_class = ReportTotalProgressSerializer

    def get_report_total_progress_list(self, request, *args, **kwargs):
        section_name = self.request.query_params.get('section_name')
        date = self.request.query_params.getlist('date')

        queryset = self.get_queryset()

        if date:
            queryset = queryset.filter(date__gte=date[0]).filter(date__lte=date[1])

        if section_name:
            queryset = queryset.filter(section_name=section_name)
        else:
            queryset = queryset.values('date').annotate(
                total_progress=Sum('total_progress'),
                month_progress_target=Sum('month_progress_target'),
                month_progress_actual=Sum('month_progress_actual'),
                section_name=Count('section_name')).order_by(
                'date')

        serializer = self.get_serializer(queryset, many=True, request=request)

        total_progress_list = serializer.data

        labels = []
        total_progress = []
        month_progress_target = []
        month_progress_actual = []
        data_list = []

        month_progress_target_num = 0
        month_progress_actual_num = 0

        for index in range(len(total_progress_list)):
            a = total_progress_list[index]
            labels.append(a.get('date'))
            total_progress.append(a.get('total_progress'))
            month_progress_target_num = month_progress_target_num + a.get('month_progress_target')
            month_progress_actual_num = month_progress_actual_num + a.get('month_progress_actual')

            month_progress_target.append(round(month_progress_target_num, 2))
            month_progress_actual.append(round(month_progress_actual_num, 2))

        data_list.append(labels)
        data_list.append(total_progress)
        data_list.append(month_progress_target)
        data_list.append(month_progress_actual)

        return DetailResponse(data=data_list)
