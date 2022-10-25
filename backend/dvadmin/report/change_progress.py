from django.db.models import Count, Sum
from dvadmin.system.models import ReportChangeProgress
from dvadmin.utils.viewset import CustomModelViewSet
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.json_response import DetailResponse, SuccessResponse, ErrorResponse


class ReportChangeProgressSerializer(CustomModelSerializer):
    """
    迁改进度报表-序列化器
    """

    class Meta:
        model = ReportChangeProgress
        fields = "__all__"
        read_only_fields = ["id"]


class ReportChangeProgressViewSet(CustomModelViewSet):
    """
    迁改进度报表接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = ReportChangeProgress.objects.all()
    serializer_class = ReportChangeProgressSerializer


class GetReportChangeProgressView(CustomModelViewSet):
    queryset = ReportChangeProgress.objects.all()
    serializer_class = ReportChangeProgressSerializer

    def get_report_change_progress_list(self, request, *args, **kwargs):
        land_section = self.request.query_params.get('land_section')
        year = self.request.query_params.get('year')

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True, request=request)

        change_progress_list = serializer.data

        labels = []
        change_progress_target = []
        change_progress_actual = []
        change_progress_predict = []
        data_list = []

        change_progress_actual_temp = []
        change_index = 0

        for index in range(len(change_progress_list)):
            a = change_progress_list[index]
            labels.append(a.get('month'))
            change_progress_target.append(a.get('change_progress_target'))

            # change_progress_actual,change_progress_predict 是有一个衔接点的，所以实际的最后一位数据和纠偏的第一个数据要一样才能完全衔接

            if a.get('change_progress_actual') == 0:
                change_progress_actual.append('-')
                if change_index == 0 and index > 0:
                    change_progress_predict[index - 1] = change_progress_actual_temp
                change_index = 1
            else:
                change_progress_actual.append(a.get('change_progress_actual'))
                change_progress_predict.append('-')
                change_progress_actual_temp = a.get('change_progress_actual')
                continue

            if a.get('change_progress_predict') == 0:
                change_progress_predict.append('-')
            else:
                change_progress_predict.append(a.get('change_progress_predict'))

        data_list.append(labels)
        data_list.append(change_progress_target)
        data_list.append(change_progress_actual)
        data_list.append(change_progress_predict)

        return DetailResponse(data=data_list)
