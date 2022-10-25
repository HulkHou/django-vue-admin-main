<template>
  <d2-container :class="{ 'page-compact': crud.pageOptions.compact }">
    <div slot="header">
      <crud-search
        ref="search"
        :options="crud.searchOptions"
        @submit="handleSearch"
      />
    </div>
    <div class="Echarts">
      <div id="main" style="width: 1400px;height:740px;"></div>
    </div>
  </d2-container>
</template>

<script>
import * as api from './api'
import { crudOptions } from './crud'
import { d2CrudPlus } from 'd2-crud-plus'

export default {
  name: 'totalProgress',
  mixins: [d2CrudPlus.crud],
  data () {
    return {}
  },
  methods: {
    getCrudOptions () {
      this.crud.searchOptions.form.section_name = 's1'
      // this.crud.searchOptions.form.query_datetime = '2020-07'
      return crudOptions(this)
    },
    pageRequest (query) {
      api.GetReportTotalProgressList(query).then(res => {
        const labels = res.data[0]
        const totalProgress = res.data[1]
        const monthProgressTarget = res.data[2]
        const monthProgressActual = res.data[3]
        labels.sort(function (a, b) {
          return a - b
        })
        // 基于准备好的dom，初始化echarts实例
        var myChart = this.$echarts.init(document.getElementById('main'))

        const symbolSize = 6

        // 指定图表的配置项和数据
        const colors = ['#5470C6', '#91CC75', '#EE6666', '#800080', '#FFFF00', '#67E0E3']
        var option = {
          color: colors,
          title: {
            text: '马东铁总体S曲线'
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross'
            }
          },
          grid: {
            top: '8%',
            bottom: '12%',
            right: '10%'
          },
          toolbox: {
            feature: {
              dataView: {
                show: true,
                readOnly: false
              },
              magicType: {
                show: true,
                type: ['line', 'bar']
              },
              restore: { show: true },
              saveAsImage: { show: true }
            }
          },
          legend: {
            data: ['工期进度线', '开累计划', '开累完成']
          },
          xAxis: [
            {
              type: 'category',
              axisTick: {
                alignWithLabel: true
              },
              data: labels
            }
          ],
          yAxis: [
            {
              type: 'value',
              position: 'left',
              alignTicks: true,
              axisLine: {
                show: true,
                lineStyle: {
                  color: colors[0]
                }
              },
              axisLabel: {
                formatter: '{value} %'
              }
            }
          ],
          dataZoom: [
            {
              type: 'slider',
              xAxisIndex: 0,
              filterMode: 'none'
            },
            {
              type: 'slider',
              yAxisIndex: 0,
              filterMode: 'none'
            },
            {
              type: 'inside',
              xAxisIndex: 0,
              filterMode: 'none'
            },
            {
              type: 'inside',
              yAxisIndex: 0,
              filterMode: 'none'
            }
          ],
          series: [
            {
              name: '工期进度线',
              type: 'line',
              yAxisIndex: 0,
              smooth: true,
              symbolSize: symbolSize,
              data: totalProgress
            },
            {
              name: '开累计划',
              type: 'line',
              yAxisIndex: 0,
              smooth: true,
              symbolSize: symbolSize,
              data: monthProgressTarget
            },
            {
              name: '开累完成',
              type: 'line',
              yAxisIndex: 0,
              smooth: true,
              symbolSize: symbolSize,
              data: monthProgressActual
            }
          ]
        }

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option)
      })
    }
  }
}
</script>

<style>

</style>
