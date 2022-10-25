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

export function GetList (query) {
  // query.limit = 999;
  return request({
    url: '/api/report/outputvalue/',
    method: 'get',
    params: query
  })
}

/**
 * 获取月度产值列表
 */
export function GetReportMonthOutputvalueList (query) {
  return request({
    url: '/api/report/outputvalue/get_report_month_outputvalue_list/',
    method: 'get',
    params: query
  })
}
