from django.db.models import Count, Sum
from dvadmin.system.models import ReportAccessibleLand
from dvadmin.utils.viewset import CustomModelViewSet
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.json_response import DetailResponse, SuccessResponse, ErrorResponse


class ReportAccessibleLandSerializer(CustomModelSerializer):
    """
    土地进场示意图-序列化器
    """

    class Meta:
        model = ReportAccessibleLand
        fields = "__all__"
        read_only_fields = ["id"]


class ReportAccessibleLandViewSet(CustomModelViewSet):
    """
    土地进场示意图接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    permission_classes = []
    queryset = ReportAccessibleLand.objects.all()
    serializer_class = ReportAccessibleLandSerializer


class GetReportAccessibleLandView(CustomModelViewSet):
    # authentication_classes = []
    permission_classes = []
    queryset = ReportAccessibleLand.objects.all()
    serializer_class = ReportAccessibleLandSerializer

    def get_report_accessible_land_list(self, request, *args, **kwargs):
        land_section = self.request.query_params.get('land_section')

        landSectionDict = {
            'A': "A段",
            'B': "B段",
            'C1': "C1段",
            'C2': "C2段"
        }
        statusDict = {
            1: "已交付土地",
            2: "先租后征土地",
            3: "未交付土地"
        }

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True, request=request)

        accessible_land_list = serializer.data

        land_section = []
        land_code = []
        status = []
        data_list = []

        for index in range(len(accessible_land_list)):
            a = accessible_land_list[index]
            land_section.append(a.get('land_section'))
            land_code.append(a.get('land_code'))
            status.append(statusDict.get(a.get('status'), "Invalid status"))

        data_list.append(land_section)
        data_list.append(land_code)
        data_list.append(status)

        return DetailResponse(data=data_list)
