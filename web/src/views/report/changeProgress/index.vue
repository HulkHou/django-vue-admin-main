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
  name: 'changeProgress',
  mixins: [d2CrudPlus.crud],
  data () {
    return {}
  },
  methods: {
    getCrudOptions () {
      this.crud.searchOptions.form.land_section = 'A'
      this.crud.searchOptions.form.year = '2022'
      return crudOptions(this)
    },
    pageRequest (query) {
      api.GetReportChangeProgressList(query).then(res => {
        const labels = res.data[0]
        const changeProgressTarget = res.data[1]
        const changeProgressActual = res.data[2]
        const changeProgressPredict = res.data[3]
        labels.sort(function (a, b) {
          return a - b
        })
        // 基于准备好的dom，初始化echarts实例
        var myChart = this.$echarts.init(document.getElementById('main'))

        const symbolSize = 6

        // 指定图表的配置项和数据
        const colors = ['#91CC75', '#5470C6', '#EE6666', '#800080', '#FFFF00', '#67E0E3']
        var option = {
          color: colors,
          title: {
            text: '迁改进度图'
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
            data: ['迁改计划值', '迁改实际值', '迁改预计值']
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
              name: '迁改计划值',
              type: 'line',
              yAxisIndex: 0,
              smooth: true,
              symbolSize: symbolSize,
              data: changeProgressTarget
            },
            {
              name: '迁改实际值',
              type: 'line',
              yAxisIndex: 0,
              smooth: true,
              symbolSize: symbolSize,
              data: changeProgressActual
            },
            {
              name: '迁改预计值',
              type: 'line',
              yAxisIndex: 0,
              smooth: true,
              symbolSize: symbolSize,
              data: changeProgressPredict
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
