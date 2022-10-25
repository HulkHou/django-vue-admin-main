import { request } from '@/api/service'

/**
 * 获取迁改进度报表列表
 */
export function GetReportChangeProgressList (query) {
  return request({
    url: '/api/report/change_progress/get_report_change_progress_list/',
    method: 'get',
    params: query
  })
}
