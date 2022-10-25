import { request } from '@/api/service'

/**
 * 获取工期进度报表列表
 */
export function GetReportTotalProgressList (query) {
  return request({
    url: '/api/report/total_progress/get_report_total_progress_list/',
    method: 'get',
    params: query
  })
}
