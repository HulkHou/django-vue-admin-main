import { request } from '@/api/service'

/**
 * 获取累计产值报表
 */
export function GetReportTotalOutputvalue (query) {
  return request({
    url: '/api/report/outputvalue/get_report_total_outputvalue/',
    method: 'get',
    params: query
  })
}
