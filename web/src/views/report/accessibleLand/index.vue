<template>
  <d2-container :class="{ 'page-compact': crud.pageOptions.compact }">
    <!--    <div slot="header">-->
    <!--      <crud-search-->
    <!--        ref="search"-->
    <!--        :options="crud.searchOptions"-->
    <!--        @submit="handleSearch"-->
    <!--      />-->
    <!--    </div>-->
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
  name: 'accessibleLand',
  mixins: [d2CrudPlus.crud],
  data () {
    return {}
  },
  methods: {
    getCrudOptions () {
      return crudOptions(this)
    },
    pageRequest (query) {
      api.GetReportAccessibleLandList(query).then(res => {
        const landSection = res.data[0]
        const landCode = res.data[1]
        const status = res.data[2]

        // 基于准备好的dom，初始化echarts实例
        const myChart = this.$echarts.init(document.getElementById('main'))

        const series = []
        for (let i = 0; i < landSection.length; i++) {
          if (landCode[i] > 0 && landCode[i] <= 43) {
            series.push({
              type: 'bar',
              stack: 'total',
              label: {
                show: false
              },
              emphasis: {
                focus: 'series'
              },
              data: (function () {
                const arr = []
                arr.push(1)
                return arr
              })(),
              name: (function () {
                let str = ''
                str = status[i]
                return str
              })()
            })
          }
          if (landCode[i] > 43 && landCode[i] <= 120) {
            series.push({
              type: 'bar',
              stack: 'total',
              label: {
                show: false
              },
              emphasis: {
                focus: 'series'
              },
              xAxisIndex: 1,
              yAxisIndex: 1,
              data: (function () {
                const arr = []
                arr.push(1)
                return arr
              })(),
              name: (function () {
                let str = ''
                str = status[i]
                return str
              })()
            })
          }
          if (landCode[i] > 120 && landCode[i] <= 215) {
            series.push({
              type: 'bar',
              stack: 'total',
              label: {
                show: false
              },
              emphasis: {
                focus: 'series'
              },
              xAxisIndex: 2,
              yAxisIndex: 2,
              data: (function () {
                const arr = []
                arr.push(1)
                return arr
              })(),
              name: (function () {
                let str = ''
                str = status[i]
                return str
              })()
            })
          }
          if (landCode[i] > 215 && landCode[i] <= 325) {
            series.push({
              type: 'bar',
              stack: 'total',
              label: {
                show: false
              },
              emphasis: {
                focus: 'series'
              },
              xAxisIndex: 3,
              yAxisIndex: 3,
              data: (function () {
                const arr = []
                arr.push(1)
                return arr
              })(),
              name: (function () {
                let str = ''
                str = status[i]
                return str
              })()
            })
          }
          if (landCode[i] > 325 && landCode[i] <= 426) {
            series.push({
              type: 'bar',
              stack: 'total',
              label: {
                show: false
              },
              emphasis: {
                focus: 'series'
              },
              xAxisIndex: 4,
              yAxisIndex: 4,
              data: (function () {
                const arr = []
                arr.push(1)
                return arr
              })(),
              name: (function () {
                let str = ''
                str = status[i]
                return str
              })()
            })
          }
        }

        const option = {
          tooltip: {
            // trigger: 'axis',
            axisPointer: {
              // Use axis to trigger tooltip
              type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
            }
          },
          legend: {},
          grid: [{
            top: '5%',
            bottom: '90%'
          }, {
            top: '15%',
            bottom: '80%'
          }, {
            top: '25%',
            bottom: '70%'
          }, {
            top: '35%',
            bottom: '60%'
          }, {
            top: '45%',
            bottom: '50%'
          }],
          xAxis: [{
            min: 0,
            max: 43,
            splitNumber: 43,
            type: 'value'
          }, {
            min: 43,
            max: 120,
            type: 'value',
            gridIndex: 1
          }, {
            min: 120,
            max: 215,
            type: 'value',
            gridIndex: 2
          }, {
            min: 215,
            max: 325,
            type: 'value',
            gridIndex: 3
          }, {
            min: 325,
            max: 426,
            type: 'value',
            gridIndex: 4
          }],
          yAxis: [{
            type: 'category',
            data: ['CH0-CH43']
          }, {
            type: 'category',
            data: ['CH44-CH120'],
            gridIndex: 1
          }, {
            type: 'category',
            data: ['CH120-CH215'],
            gridIndex: 2
          }, {
            type: 'category',
            data: ['CH215-CH325'],
            gridIndex: 3
          }, {
            type: 'category',
            data: ['CH325-CH426'],
            gridIndex: 4
          }],
          series: series
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
