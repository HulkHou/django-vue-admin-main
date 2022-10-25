import { request } from '@/api/service'

/**
 * 获取可进场土地示意图报表列表
 */
export function GetReportAccessibleLandList (query) {
  return request({
    url: '/api/report/accessible_land/get_report_accessible_land_list/',
    method: 'get',
    params: query
  })
}
