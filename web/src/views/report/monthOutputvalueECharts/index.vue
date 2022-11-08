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
  name: 'monthOutputvalueECharts',
  mixins: [d2CrudPlus.crud],
  data () {
    return {}
  },
  methods: {
    getCrudOptions () {
      // this.crud.searchOptions.form.section = 's1'
      this.crud.searchOptions.form.year = '2022'
      return crudOptions(this)
    },
    pageRequest (query) {
      api.GetReportMonthOutputvalueList(query).then(res => {
        const labels = res.data[0]
        // const outputValueLowest = res.data[1]
        const outputValueTarget = res.data[2]
        const outputValueActual = res.data[3]
        const outputValueLowestSum = res.data[4]
        const outputValueTargetSum = res.data[5]
        const outputValueActualSum = res.data[6]
        labels.sort(function (a, b) {
          return a - b
        })
        // 基于准备好的dom，初始化echarts实例
        var myChart = this.$echarts.init(document.getElementById('main'))

        // 指定图表的配置项和数据
        const colors = ['#91CC75', '#5470C6', '#EE6666', '#91CC75', '#5470C6']
        var option = {
          color: colors,
          title: {
            text: '月度产值计划与实际直方图和曲线'
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross'
            }
          },
          grid: {
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
            data: ['月度产值-保底计划', '月度产值-计划', '月度产值-实际', '2021年累计产值（倍增）', '累计产值-计划', '累计产值-实际']
          },
          xAxis: [
            {
              type: 'category',
              axisTick: {
                alignWithLabel: true
              },
              // prettier-ignore
              data: (function () {
                const list = []
                for (let i = 0; i < labels.length; i++) {
                  list.push(labels[i] + ' 月')
                }
                return list
              })()
            }
          ],
          yAxis: [
            {
              type: 'value',
              name: '累计产值',
              position: 'right',
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
            },
            {
              type: 'value',
              name: '月度产值',
              position: 'left',
              alignTicks: true,
              offset: 0,
              axisLine: {
                show: true,
                lineStyle: {
                  color: colors[1]
                }
              },
              axisLabel: {
                formatter: '{value} %'
              }
            }
          ],
          series: [
            // {
            //   name: '月度产值-保底计划',
            //   type: 'bar',
            //   yAxisIndex: 1,
            //   data: outputValueLowest
            // },
            {
              name: '月度产值-计划',
              type: 'bar',
              yAxisIndex: 1,
              label: {
                show: true,
                position: 'top'
              },
              data: outputValueTarget
            },
            {
              name: '月度产值-实际',
              type: 'bar',
              yAxisIndex: 1,
              label: {
                show: true,
                position: 'top'
              },
              data: outputValueActual
            },
            {
              name: '2021年累计产值（倍增）',
              type: 'line',
              yAxisIndex: 0,
              smooth: true,
              data: outputValueLowestSum
            },
            {
              name: '累计产值-计划',
              type: 'line',
              yAxisIndex: 0,
              smooth: true,
              data: outputValueTargetSum
            },
            {
              name: '累计产值-实际',
              type: 'line',
              yAxisIndex: 0,
              smooth: true,
              data: outputValueActualSum
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
