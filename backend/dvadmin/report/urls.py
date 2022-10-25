from django.urls import path
from rest_framework import routers

from dvadmin.report.output_value_view import OutputvalueViewSet
from dvadmin.report.month_output_value_view import ReportMonthOutputvalueViewSet
from dvadmin.report.month_output_value_view import GetReportMonthOutputvalueView
from dvadmin.report.total_output_value_view import GetReportTotalOutputvalueView

from dvadmin.report.total_progress import GetReportTotalProgressView, ReportTotalProgressViewSet
from dvadmin.report.accessible_land import GetReportAccessibleLandView, ReportAccessibleLandViewSet
from dvadmin.report.change_progress import GetReportChangeProgressView, ReportChangeProgressViewSet


system_url = routers.SimpleRouter()
system_url.register(r'outputvalue', OutputvalueViewSet)
system_url.register(r'report_month_outputvalue', ReportMonthOutputvalueViewSet)

system_url.register(r'total_progress', ReportTotalProgressViewSet)
system_url.register(r'accessible_land', ReportAccessibleLandViewSet)
system_url.register(r'change_progress', ReportChangeProgressViewSet)


urlpatterns = [
    path('outputvalue/get_report_month_outputvalue/',
         GetReportMonthOutputvalueView.as_view({'get': 'get_report_month_outputvalue'})),
    path('outputvalue/get_report_month_outputvalue_list/',
         GetReportMonthOutputvalueView.as_view({'get': 'get_report_month_outputvalue_list'})),
    path('outputvalue/get_report_total_outputvalue/',
         GetReportTotalOutputvalueView.as_view({'get': 'get_report_total_outputvalue'})),

    path('total_progress/get_report_total_progress_list/',
         GetReportTotalProgressView.as_view({'get': 'get_report_total_progress_list'})),
    path('accessible_land/get_report_accessible_land_list/',
         GetReportAccessibleLandView.as_view({'get': 'get_report_accessible_land_list'})),
    path('change_progress/get_report_change_progress_list/',
         GetReportChangeProgressView.as_view({'get': 'get_report_change_progress_list'})),
]
urlpatterns += system_url.urls
