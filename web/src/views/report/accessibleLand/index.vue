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
      <div id="main" style="width: 1400px;height:1600px;"></div>
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
      this.crud.searchOptions.form.land_section = 'CH0-45'
      return crudOptions(this)
    },
    pageRequest (query) {
      api.GetReportAccessibleLandList(query).then(res => {
        const landSection = res.data[0]
        const landCode = res.data[1]
        const status = res.data[2]

        // 基于准备好的dom，初始化echarts实例
        const colors = ['#6495ED', '#FF0000', '#800080']
        const myChart = this.$echarts.init(document.getElementById('main'))
        const seriesData = []
        let option = {}
        let x = 0
        let y = 0
        if (landSection[0] === 'CH0-45') {
          for (let i = 0; i < landSection.length; i++) {
            if (landCode[i] > 0 && landCode[i] <= 50) {
              x = 0
              y = 0
            } else if (landCode[i] > 50 && landCode[i] <= 100) {
              x = 1
              y = 1
            } else if (landCode[i] > 100 && landCode[i] <= 150) {
              x = 2
              y = 2
            } else if (landCode[i] > 150 && landCode[i] <= 200) {
              x = 3
              y = 3
            } else if (landCode[i] > 200 && landCode[i] <= 250) {
              x = 4
              y = 4
            } else if (landCode[i] > 250 && landCode[i] <= 300) {
              x = 5
              y = 5
            } else if (landCode[i] > 300 && landCode[i] <= 350) {
              x = 6
              y = 6
            } else if (landCode[i] > 350 && landCode[i] <= 400) {
              x = 7
              y = 7
            } else if (landCode[i] > 400 && landCode[i] <= 450) {
              x = 8
              y = 8
            }
            seriesData.push({
              type: 'bar',
              stack: 'total',
              label: {
                show: false
              },
              emphasis: {
                focus: 'series'
              },
              // data: (function () {
              //   const arr = []
              //   arr.push(1)
              //   return arr
              // })(),
              data: [1],
              xAxisIndex: x,
              yAxisIndex: y,
              name: (function () {
                let str = ''
                str = status[i]
                return str
              })()
            })
          }
          option = {
            color: colors,
            tooltip: {
              // trigger: 'axis',
              axisPointer: {
                // Use axis to trigger tooltip
                type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
              }
            },
            legend: {},
            grid: [{
              top: '2%',
              bottom: '96%'
            }, {
              top: '6%',
              bottom: '92%'
            }, {
              top: '10%',
              bottom: '88%'
            }, {
              top: '14%',
              bottom: '84%'
            }, {
              top: '18%',
              bottom: '80%'
            }, {
              top: '22%',
              bottom: '76%'
            }, {
              top: '26%',
              bottom: '72%'
            }, {
              top: '30%',
              bottom: '68%'
            }, {
              top: '34%',
              bottom: '64%'
            }],
            xAxis: [{
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10
                }
              },
              type: 'value',
              splitLine: {
                show: true
              }
            }, {
              min: 50,
              max: 100,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10
                }
              },
              type: 'value',
              gridIndex: 1
            }, {
              min: 100,
              max: 150,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10
                }
              },
              type: 'value',
              gridIndex: 2
            }, {
              min: 150,
              max: 200,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10
                }
              },
              type: 'value',
              gridIndex: 3
            }, {
              min: 200,
              max: 250,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10
                }
              },
              type: 'value',
              gridIndex: 4
            }, {
              min: 250,
              max: 300,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10
                }
              },
              type: 'value',
              gridIndex: 5
            }, {
              min: 300,
              max: 350,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10
                }
              },
              type: 'value',
              gridIndex: 6
            }, {
              min: 350,
              max: 400,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10
                }
              },
              type: 'value',
              gridIndex: 7
            }, {
              min: 400,
              max: 450,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10
                }
              },
              type: 'value',
              gridIndex: 8
            }],
            yAxis: [{
              type: 'category',
              data: ['CH0-CH5']
            }, {
              type: 'category',
              data: ['CH5-CH10'],
              gridIndex: 1
            }, {
              type: 'category',
              data: ['CH10-CH15'],
              gridIndex: 2
            }, {
              type: 'category',
              data: ['CH15-CH20'],
              gridIndex: 3
            }, {
              type: 'category',
              data: ['CH20-CH25'],
              gridIndex: 4
            }, {
              type: 'category',
              data: ['CH25-CH30'],
              gridIndex: 5
            }, {
              type: 'category',
              data: ['CH30-CH35'],
              gridIndex: 6
            }, {
              type: 'category',
              data: ['CH35-CH40'],
              gridIndex: 7
            }, {
              type: 'category',
              data: ['CH40-CH45'],
              gridIndex: 8
            }],
            series: seriesData
          }
        } else if (landSection[0] === 'CH45-120') {
          let start = 450
          const end = 1200
          let z = 0
          for (let i = 0; i < landSection.length; i++) {
            if (landCode[i] > start && landCode[i] <= start + 50 && landCode[i] <= end) {
              x = z
              y = z
            } else {
              z = z + 1
              x = z
              y = z
              start = start + 50
            }
            seriesData.push({
              type: 'bar',
              stack: 'total',
              label: {
                show: false
              },
              emphasis: {
                focus: 'series'
              },
              data: [1],
              xAxisIndex: x,
              yAxisIndex: y,
              name: (function () {
                let str = ''
                str = status[i]
                return str
              })()
            })
          }
          option = {
            color: colors,
            tooltip: {
              // trigger: 'axis',
              axisPointer: {
                // Use axis to trigger tooltip
                type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
              }
            },
            legend: {},
            grid: [{
              top: '2%',
              bottom: '96%'
            }, {
              top: '6%',
              bottom: '92%'
            }, {
              top: '10%',
              bottom: '88%'
            }, {
              top: '14%',
              bottom: '84%'
            }, {
              top: '18%',
              bottom: '80%'
            }, {
              top: '22%',
              bottom: '76%'
            }, {
              top: '26%',
              bottom: '72%'
            }, {
              top: '30%',
              bottom: '68%'
            }, {
              top: '34%',
              bottom: '64%'
            }, {
              top: '38%',
              bottom: '60%'
            }, {
              top: '42%',
              bottom: '56%'
            }, {
              top: '46%',
              bottom: '52%'
            }, {
              top: '50%',
              bottom: '48%'
            }, {
              top: '54%',
              bottom: '44%'
            }, {
              top: '58%',
              bottom: '40%'
            }],
            xAxis: [{
              min: 0,
              max: 50,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value'
            }, {
              min: 50,
              max: 100,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value',
              gridIndex: 1
            }, {
              min: 100,
              max: 150,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value',
              gridIndex: 2
            }, {
              min: 150,
              max: 200,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value',
              gridIndex: 3
            }, {
              min: 200,
              max: 250,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value',
              gridIndex: 4
            }, {
              min: 250,
              max: 300,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value',
              gridIndex: 5
            }, {
              min: 300,
              max: 350,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value',
              gridIndex: 6
            }, {
              min: 350,
              max: 400,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value',
              gridIndex: 7
            }, {
              min: 400,
              max: 450,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value',
              gridIndex: 8
            }, {
              min: 450,
              max: 500,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value',
              gridIndex: 9
            }, {
              min: 500,
              max: 550,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value',
              gridIndex: 10
            }, {
              min: 550,
              max: 600,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value',
              gridIndex: 11
            }, {
              min: 600,
              max: 650,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value',
              gridIndex: 12
            }, {
              min: 650,
              max: 700,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value',
              gridIndex: 13
            }, {
              min: 700,
              max: 750,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 45
                }
              },
              type: 'value',
              gridIndex: 14
            }],
            yAxis: [{
              type: 'category',
              data: ['CH45-50']
            }, {
              type: 'category',
              data: ['CH50-55'],
              gridIndex: 1
            }, {
              type: 'category',
              data: ['CH55-60'],
              gridIndex: 2
            }, {
              type: 'category',
              data: ['CH60-65'],
              gridIndex: 3
            }, {
              type: 'category',
              data: ['CH65-70'],
              gridIndex: 4
            }, {
              type: 'category',
              data: ['CH70-75'],
              gridIndex: 5
            }, {
              type: 'category',
              data: ['CH75-80'],
              gridIndex: 6
            }, {
              type: 'category',
              data: ['CH80-85'],
              gridIndex: 7
            }, {
              type: 'category',
              data: ['CH85-90'],
              gridIndex: 8
            }, {
              type: 'category',
              data: ['CH90-95'],
              gridIndex: 9
            }, {
              type: 'category',
              data: ['CH95-100'],
              gridIndex: 10
            }, {
              type: 'category',
              data: ['CH100-105'],
              gridIndex: 11
            }, {
              type: 'category',
              data: ['CH105-110'],
              gridIndex: 12
            }, {
              type: 'category',
              data: ['CH110-115'],
              gridIndex: 13
            }, {
              type: 'category',
              data: ['CH115-120'],
              gridIndex: 14
            }],
            series: seriesData
          }
        } else if (landSection[0] === 'CH120-215') {
          let start = 1200
          const end = 2150
          let z = 0
          for (let i = 0; i < landSection.length; i++) {
            if (landCode[i] > start && landCode[i] <= start + 50 && landCode[i] <= end) {
              x = z
              y = z
            } else {
              z = z + 1
              x = z
              y = z
              start = start + 50
            }
            seriesData.push({
              type: 'bar',
              stack: 'total',
              label: {
                show: false
              },
              emphasis: {
                focus: 'series'
              },
              data: [1],
              xAxisIndex: x,
              yAxisIndex: y,
              name: (function () {
                let str = ''
                str = status[i]
                return str
              })()
            })
          }
          option = {
            color: colors,
            tooltip: {
              // trigger: 'axis',
              axisPointer: {
                // Use axis to trigger tooltip
                type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
              }
            },
            legend: {},
            grid: [{
              top: '2%',
              bottom: '96%'
            }, {
              top: '6%',
              bottom: '92%'
            }, {
              top: '10%',
              bottom: '88%'
            }, {
              top: '14%',
              bottom: '84%'
            }, {
              top: '18%',
              bottom: '80%'
            }, {
              top: '22%',
              bottom: '76%'
            }, {
              top: '26%',
              bottom: '72%'
            }, {
              top: '30%',
              bottom: '68%'
            }, {
              top: '34%',
              bottom: '64%'
            }, {
              top: '38%',
              bottom: '60%'
            }, {
              top: '42%',
              bottom: '56%'
            }, {
              top: '46%',
              bottom: '52%'
            }, {
              top: '50%',
              bottom: '48%'
            }, {
              top: '54%',
              bottom: '44%'
            }, {
              top: '58%',
              bottom: '40%'
            }, {
              top: '62%',
              bottom: '36%'
            }, {
              top: '66%',
              bottom: '32%'
            }, {
              top: '70%',
              bottom: '28%'
            }, {
              top: '74%',
              bottom: '24%'
            }],
            xAxis: [{
              min: 0,
              max: 50,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value'
            }, {
              min: 50,
              max: 100,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 1
            }, {
              min: 100,
              max: 150,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 2
            }, {
              min: 150,
              max: 200,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 3
            }, {
              min: 200,
              max: 250,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 4
            }, {
              min: 250,
              max: 300,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 5
            }, {
              min: 300,
              max: 350,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 6
            }, {
              min: 350,
              max: 400,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 7
            }, {
              min: 400,
              max: 450,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 8
            }, {
              min: 450,
              max: 500,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 9
            }, {
              min: 500,
              max: 550,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 10
            }, {
              min: 550,
              max: 600,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 11
            }, {
              min: 600,
              max: 650,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 12
            }, {
              min: 650,
              max: 700,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 13
            }, {
              min: 700,
              max: 750,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 14
            }, {
              min: 750,
              max: 800,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 15
            }, {
              min: 800,
              max: 850,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 16
            }, {
              min: 850,
              max: 900,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 17
            }, {
              min: 900,
              max: 950,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 120
                }
              },
              type: 'value',
              gridIndex: 18
            }],
            yAxis: [{
              type: 'category',
              data: ['CH120-125']
            }, {
              type: 'category',
              data: ['CH125-130'],
              gridIndex: 1
            }, {
              type: 'category',
              data: ['CH130-135'],
              gridIndex: 2
            }, {
              type: 'category',
              data: ['CH135-140'],
              gridIndex: 3
            }, {
              type: 'category',
              data: ['CH140-145'],
              gridIndex: 4
            }, {
              type: 'category',
              data: ['CH145-150'],
              gridIndex: 5
            }, {
              type: 'category',
              data: ['CH150-155'],
              gridIndex: 6
            }, {
              type: 'category',
              data: ['CH155-160'],
              gridIndex: 7
            }, {
              type: 'category',
              data: ['CH160-165'],
              gridIndex: 8
            }, {
              type: 'category',
              data: ['CH165-170'],
              gridIndex: 9
            }, {
              type: 'category',
              data: ['CH170-175'],
              gridIndex: 10
            }, {
              type: 'category',
              data: ['CH175-180'],
              gridIndex: 11
            }, {
              type: 'category',
              data: ['CH180-185'],
              gridIndex: 12
            }, {
              type: 'category',
              data: ['CH185-190'],
              gridIndex: 13
            }, {
              type: 'category',
              data: ['CH190-195'],
              gridIndex: 14
            }, {
              type: 'category',
              data: ['CH195-200'],
              gridIndex: 15
            }, {
              type: 'category',
              data: ['CH200-205'],
              gridIndex: 16
            }, {
              type: 'category',
              data: ['CH205-210'],
              gridIndex: 17
            }, {
              type: 'category',
              data: ['CH210-215'],
              gridIndex: 18
            }],
            series: seriesData
          }
        } else if (landSection[0] === 'CH215-325') {
          let start = 2150
          const end = 3250
          let z = 0
          for (let i = 0; i < landSection.length; i++) {
            if (landCode[i] > start && landCode[i] <= start + 50 && landCode[i] <= end) {
              x = z
              y = z
            } else {
              z = z + 1
              x = z
              y = z
              start = start + 50
            }
            seriesData.push({
              type: 'bar',
              stack: 'total',
              label: {
                show: false
              },
              emphasis: {
                focus: 'series'
              },
              data: [1],
              xAxisIndex: x,
              yAxisIndex: y,
              name: (function () {
                let str = ''
                str = status[i]
                return str
              })()
            })
          }
          option = {
            color: colors,
            tooltip: {
              // trigger: 'axis',
              axisPointer: {
                // Use axis to trigger tooltip
                type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
              }
            },
            legend: {},
            grid: [{
              top: '2%',
              bottom: '96%'
            }, {
              top: '6%',
              bottom: '92%'
            }, {
              top: '10%',
              bottom: '88%'
            }, {
              top: '14%',
              bottom: '84%'
            }, {
              top: '18%',
              bottom: '80%'
            }, {
              top: '22%',
              bottom: '76%'
            }, {
              top: '26%',
              bottom: '72%'
            }, {
              top: '30%',
              bottom: '68%'
            }, {
              top: '34%',
              bottom: '64%'
            }, {
              top: '38%',
              bottom: '60%'
            }, {
              top: '42%',
              bottom: '56%'
            }, {
              top: '46%',
              bottom: '52%'
            }, {
              top: '50%',
              bottom: '48%'
            }, {
              top: '54%',
              bottom: '44%'
            }, {
              top: '58%',
              bottom: '40%'
            }, {
              top: '62%',
              bottom: '36%'
            }, {
              top: '66%',
              bottom: '32%'
            }, {
              top: '70%',
              bottom: '28%'
            }, {
              top: '74%',
              bottom: '24%'
            }, {
              top: '78%',
              bottom: '20%'
            }, {
              top: '82%',
              bottom: '16%'
            }, {
              top: '86%',
              bottom: '12%'
            }],
            xAxis: [{
              min: 0,
              max: 50,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value'
            }, {
              min: 50,
              max: 100,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 1
            }, {
              min: 100,
              max: 150,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 2
            }, {
              min: 150,
              max: 200,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 3
            }, {
              min: 200,
              max: 250,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 4
            }, {
              min: 250,
              max: 300,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 5
            }, {
              min: 300,
              max: 350,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 6
            }, {
              min: 350,
              max: 400,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 7
            }, {
              min: 400,
              max: 450,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 8
            }, {
              min: 450,
              max: 500,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 9
            }, {
              min: 500,
              max: 550,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 10
            }, {
              min: 550,
              max: 600,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 11
            }, {
              min: 600,
              max: 650,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 12
            }, {
              min: 650,
              max: 700,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 13
            }, {
              min: 700,
              max: 750,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 14
            }, {
              min: 750,
              max: 800,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 15
            }, {
              min: 800,
              max: 850,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 16
            }, {
              min: 850,
              max: 900,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 17
            }, {
              min: 900,
              max: 950,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 18
            }, {
              min: 950,
              max: 1000,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 19
            }, {
              min: 1000,
              max: 1050,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 20
            }, {
              min: 1050,
              max: 1100,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 215
                }
              },
              type: 'value',
              gridIndex: 21
            }],
            yAxis: [{
              type: 'category',
              data: ['CH215-220']
            }, {
              type: 'category',
              data: ['CH220-225'],
              gridIndex: 1
            }, {
              type: 'category',
              data: ['CH225-230'],
              gridIndex: 2
            }, {
              type: 'category',
              data: ['CH230-235'],
              gridIndex: 3
            }, {
              type: 'category',
              data: ['CH235-240'],
              gridIndex: 4
            }, {
              type: 'category',
              data: ['CH240-245'],
              gridIndex: 5
            }, {
              type: 'category',
              data: ['CH245-250'],
              gridIndex: 6
            }, {
              type: 'category',
              data: ['CH250-255'],
              gridIndex: 7
            }, {
              type: 'category',
              data: ['CH255-260'],
              gridIndex: 8
            }, {
              type: 'category',
              data: ['CH260-265'],
              gridIndex: 9
            }, {
              type: 'category',
              data: ['CH265-270'],
              gridIndex: 10
            }, {
              type: 'category',
              data: ['CH270-275'],
              gridIndex: 11
            }, {
              type: 'category',
              data: ['CH275-280'],
              gridIndex: 12
            }, {
              type: 'category',
              data: ['CH280-285'],
              gridIndex: 13
            }, {
              type: 'category',
              data: ['CH285-290'],
              gridIndex: 14
            }, {
              type: 'category',
              data: ['CH290-295'],
              gridIndex: 15
            }, {
              type: 'category',
              data: ['CH295-300'],
              gridIndex: 16
            }, {
              type: 'category',
              data: ['CH300-305'],
              gridIndex: 17
            }, {
              type: 'category',
              data: ['CH305-310'],
              gridIndex: 18
            }, {
              type: 'category',
              data: ['CH310-315'],
              gridIndex: 19
            }, {
              type: 'category',
              data: ['CH315-320'],
              gridIndex: 20
            }, {
              type: 'category',
              data: ['CH320-325'],
              gridIndex: 21
            }],
            series: seriesData
          }
        } else if (landSection[0] === 'CH325-426') {
          let start = 3250
          const end = 4260
          let z = 0
          for (let i = 0; i < landSection.length; i++) {
            if (landCode[i] > start && landCode[i] <= start + 50 && landCode[i] <= end) {
              x = z
              y = z
            } else {
              z = z + 1
              x = z
              y = z
              start = start + 50
            }
            seriesData.push({
              type: 'bar',
              stack: 'total',
              label: {
                show: false
              },
              emphasis: {
                focus: 'series'
              },
              data: [1],
              xAxisIndex: x,
              yAxisIndex: y,
              name: (function () {
                let str = ''
                str = status[i]
                return str
              })()
            })
          }
          option = {
            color: colors,
            tooltip: {
              // trigger: 'axis',
              axisPointer: {
                // Use axis to trigger tooltip
                type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
              }
            },
            legend: {},
            grid: [{
              top: '2%',
              bottom: '96%'
            }, {
              top: '6%',
              bottom: '92%'
            }, {
              top: '10%',
              bottom: '88%'
            }, {
              top: '14%',
              bottom: '84%'
            }, {
              top: '18%',
              bottom: '80%'
            }, {
              top: '22%',
              bottom: '76%'
            }, {
              top: '26%',
              bottom: '72%'
            }, {
              top: '30%',
              bottom: '68%'
            }, {
              top: '34%',
              bottom: '64%'
            }, {
              top: '38%',
              bottom: '60%'
            }, {
              top: '42%',
              bottom: '56%'
            }, {
              top: '46%',
              bottom: '52%'
            }, {
              top: '50%',
              bottom: '48%'
            }, {
              top: '54%',
              bottom: '44%'
            }, {
              top: '58%',
              bottom: '40%'
            }, {
              top: '62%',
              bottom: '36%'
            }, {
              top: '66%',
              bottom: '32%'
            }, {
              top: '70%',
              bottom: '28%'
            }, {
              top: '74%',
              bottom: '24%'
            }, {
              top: '78%',
              bottom: '20%'
            }, {
              top: '82%',
              bottom: '16%'
            }],
            xAxis: [{
              min: 0,
              max: 50,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value'
            }, {
              min: 50,
              max: 100,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 1
            }, {
              min: 100,
              max: 150,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 2
            }, {
              min: 150,
              max: 200,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 3
            }, {
              min: 200,
              max: 250,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 4
            }, {
              min: 250,
              max: 300,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 5
            }, {
              min: 300,
              max: 350,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 6
            }, {
              min: 350,
              max: 400,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 7
            }, {
              min: 400,
              max: 450,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 8
            }, {
              min: 450,
              max: 500,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 9
            }, {
              min: 500,
              max: 550,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 10
            }, {
              min: 550,
              max: 600,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 11
            }, {
              min: 600,
              max: 650,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 12
            }, {
              min: 650,
              max: 700,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 13
            }, {
              min: 700,
              max: 750,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 14
            }, {
              min: 750,
              max: 800,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 15
            }, {
              min: 800,
              max: 850,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 16
            }, {
              min: 850,
              max: 900,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 17
            }, {
              min: 900,
              max: 950,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 18
            }, {
              min: 950,
              max: 1000,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 19
            }, {
              min: 1000,
              max: 1010,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 325
                }
              },
              type: 'value',
              gridIndex: 20
            }],
            yAxis: [{
              type: 'category',
              data: ['CH325-330']
            }, {
              type: 'category',
              data: ['CH330-335'],
              gridIndex: 1
            }, {
              type: 'category',
              data: ['CH335-340'],
              gridIndex: 2
            }, {
              type: 'category',
              data: ['CH340-345'],
              gridIndex: 3
            }, {
              type: 'category',
              data: ['CH345-350'],
              gridIndex: 4
            }, {
              type: 'category',
              data: ['CH350-355'],
              gridIndex: 5
            }, {
              type: 'category',
              data: ['CH355-360'],
              gridIndex: 6
            }, {
              type: 'category',
              data: ['CH360-365'],
              gridIndex: 7
            }, {
              type: 'category',
              data: ['CH365-370'],
              gridIndex: 8
            }, {
              type: 'category',
              data: ['CH370-375'],
              gridIndex: 9
            }, {
              type: 'category',
              data: ['CH375-380'],
              gridIndex: 10
            }, {
              type: 'category',
              data: ['CH380-385'],
              gridIndex: 11
            }, {
              type: 'category',
              data: ['CH385-390'],
              gridIndex: 12
            }, {
              type: 'category',
              data: ['CH390-395'],
              gridIndex: 13
            }, {
              type: 'category',
              data: ['CH395-400'],
              gridIndex: 14
            }, {
              type: 'category',
              data: ['CH400-405'],
              gridIndex: 15
            }, {
              type: 'category',
              data: ['CH405-410'],
              gridIndex: 16
            }, {
              type: 'category',
              data: ['CH410-415'],
              gridIndex: 17
            }, {
              type: 'category',
              data: ['CH415-420'],
              gridIndex: 18
            }, {
              type: 'category',
              data: ['CH420-425'],
              gridIndex: 19
            }, {
              type: 'category',
              data: ['CH425-426'],
              gridIndex: 20
            }],
            series: seriesData
          }
        } else if (landSection[0] === 'CH426-508') {
          let start = 4260
          const end = 5080
          let z = 0
          for (let i = 0; i < landSection.length; i++) {
            if (landCode[i] > start && landCode[i] <= start + 50 && landCode[i] <= end) {
              x = z
              y = z
            } else {
              z = z + 1
              x = z
              y = z
              start = start + 50
            }
            seriesData.push({
              type: 'bar',
              stack: 'total',
              label: {
                show: false
              },
              emphasis: {
                focus: 'series'
              },
              data: [1],
              xAxisIndex: x,
              yAxisIndex: y,
              name: (function () {
                let str = ''
                str = status[i]
                return str
              })()
            })
          }
          option = {
            color: colors,
            tooltip: {
              // trigger: 'axis',
              axisPointer: {
                // Use axis to trigger tooltip
                type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
              }
            },
            legend: {},
            grid: [{
              top: '2%',
              bottom: '96%'
            }, {
              top: '6%',
              bottom: '92%'
            }, {
              top: '10%',
              bottom: '88%'
            }, {
              top: '14%',
              bottom: '84%'
            }, {
              top: '18%',
              bottom: '80%'
            }, {
              top: '22%',
              bottom: '76%'
            }, {
              top: '26%',
              bottom: '72%'
            }, {
              top: '30%',
              bottom: '68%'
            }, {
              top: '34%',
              bottom: '64%'
            }, {
              top: '38%',
              bottom: '60%'
            }, {
              top: '42%',
              bottom: '56%'
            }, {
              top: '46%',
              bottom: '52%'
            }, {
              top: '50%',
              bottom: '48%'
            }, {
              top: '54%',
              bottom: '44%'
            }, {
              top: '58%',
              bottom: '40%'
            }, {
              top: '62%',
              bottom: '36%'
            }, {
              top: '66%',
              bottom: '32%'
            }],
            xAxis: [{
              min: 0,
              max: 50,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value'
            }, {
              min: 50,
              max: 100,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 1
            }, {
              min: 100,
              max: 150,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 2
            }, {
              min: 150,
              max: 200,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 3
            }, {
              min: 200,
              max: 250,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 4
            }, {
              min: 250,
              max: 300,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 5
            }, {
              min: 300,
              max: 350,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 6
            }, {
              min: 350,
              max: 400,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 7
            }, {
              min: 400,
              max: 450,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 8
            }, {
              min: 450,
              max: 500,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 9
            }, {
              min: 500,
              max: 550,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 10
            }, {
              min: 550,
              max: 600,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 11
            }, {
              min: 600,
              max: 650,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 12
            }, {
              min: 650,
              max: 700,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 13
            }, {
              min: 700,
              max: 750,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 14
            }, {
              min: 750,
              max: 800,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 15
            }, {
              min: 800,
              max: 820,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 426
                }
              },
              type: 'value',
              gridIndex: 16
            }],
            yAxis: [{
              type: 'category',
              data: ['CH426-431']
            }, {
              type: 'category',
              data: ['CH431-436'],
              gridIndex: 1
            }, {
              type: 'category',
              data: ['CH436-441'],
              gridIndex: 2
            }, {
              type: 'category',
              data: ['CH441-446'],
              gridIndex: 3
            }, {
              type: 'category',
              data: ['CH446-451'],
              gridIndex: 4
            }, {
              type: 'category',
              data: ['CH451-456'],
              gridIndex: 5
            }, {
              type: 'category',
              data: ['CH456-461'],
              gridIndex: 6
            }, {
              type: 'category',
              data: ['CH461-466'],
              gridIndex: 7
            }, {
              type: 'category',
              data: ['CH466-471'],
              gridIndex: 8
            }, {
              type: 'category',
              data: ['CH471-476'],
              gridIndex: 9
            }, {
              type: 'category',
              data: ['CH476-481'],
              gridIndex: 10
            }, {
              type: 'category',
              data: ['CH481-486'],
              gridIndex: 11
            }, {
              type: 'category',
              data: ['CH486-491'],
              gridIndex: 12
            }, {
              type: 'category',
              data: ['CH491-496'],
              gridIndex: 13
            }, {
              type: 'category',
              data: ['CH496-501'],
              gridIndex: 14
            }, {
              type: 'category',
              data: ['CH501-506'],
              gridIndex: 15
            }, {
              type: 'category',
              data: ['CH506-508'],
              gridIndex: 16
            }],
            series: seriesData
          }
        } else if (landSection[0] === 'CH508-523') {
          let start = 5080
          const end = 5230
          let z = 0
          for (let i = 0; i < landSection.length; i++) {
            if (landCode[i] > start && landCode[i] <= start + 50 && landCode[i] <= end) {
              x = z
              y = z
            } else {
              z = z + 1
              x = z
              y = z
              start = start + 50
            }
            seriesData.push({
              type: 'bar',
              stack: 'total',
              label: {
                show: false
              },
              emphasis: {
                focus: 'series'
              },
              data: [1],
              xAxisIndex: x,
              yAxisIndex: y,
              name: (function () {
                let str = ''
                str = status[i]
                return str
              })()
            })
          }
          option = {
            color: colors,
            tooltip: {
              // trigger: 'axis',
              axisPointer: {
                // Use axis to trigger tooltip
                type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
              }
            },
            legend: {},
            grid: [{
              top: '2%',
              bottom: '96%'
            }, {
              top: '6%',
              bottom: '92%'
            }, {
              top: '10%',
              bottom: '88%'
            }],
            xAxis: [{
              min: 0,
              max: 50,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 508
                }
              },
              type: 'value'
            }, {
              min: 50,
              max: 100,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 508
                }
              },
              type: 'value',
              gridIndex: 1
            }, {
              min: 100,
              max: 150,
              axisLabel: {
                formatter: function (value, index) {
                  return value / 10 + 508
                }
              },
              type: 'value',
              gridIndex: 2
            }],
            yAxis: [{
              type: 'category',
              data: ['CH508-513']
            }, {
              type: 'category',
              data: ['CH513-518'],
              gridIndex: 1
            }, {
              type: 'category',
              data: ['CH518-523'],
              gridIndex: 2
            }],
            series: seriesData
          }
        }
        // 重新渲染
        document.getElementById('main').setAttribute('_echarts_instance_', '')
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option, true)
      })
    }
  }
}
</script>

<style>

</style>
