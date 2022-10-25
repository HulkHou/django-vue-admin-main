import { request } from '@/api/service'

/**
 * 获取月度产值报表
 */
export function GetReportMonthOutputvalue (query) {
  return request({
    url: '/api/report/outputvalue/get_report_month_outputvalue/',
    method: 'get',
    params: query
  })
}
