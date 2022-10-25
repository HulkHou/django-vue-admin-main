export const crudOptions = (vm) => {
  return {
    columns: [
      {
        title: '分部',
        key: 'section',
        sortable: true,
        search: {
          disabled: false
        },
        width: 90,
        type: 'select',
        dict: {
          data: [{
            value: 's1',
            label: '一分部'
          }, {
            value: 's2',
            label: '二分部'
          }, {
            value: 's3',
            label: '三分部'
          }, {
            value: 's4',
            label: '四分部'
          }, {
            value: 's5',
            label: '五分部'
          }, {
            value: 's6-B',
            label: '六分部B段'
          }, {
            value: 's6-C',
            label: '六分部C段'
          }, {
            value: 's7',
            label: '七分部'
          }, {
            value: 's8',
            label: '八分部'
          }, {
            value: 's9',
            label: '九分部'
          }, {
            value: 's10',
            label: '十分部'
          }, {
            value: 's11',
            label: '十一分部'
          }]
        },
        form: {
          value: true,
          component: {
            span: 12,
            placeholder: '请选择分部'
          }
        }
      }, {
        title: '年度',
        key: 'year',
        sortable: true,
        search: {
          disabled: false
        },
        width: 90,
        type: 'select',
        dict: {
          data: [{
            value: '2017',
            label: '2017'
          }, {
            value: '2018',
            label: '2018'
          }, {
            value: '2019',
            label: '2019'
          }, {
            value: '2020',
            label: '2020'
          }, {
            value: '2021',
            label: '2021'
          }, {
            value: '2022',
            label: '2022'
          }, {
            value: '2023',
            label: '2023'
          }, {
            value: '2024',
            label: '2024'
          }, {
            value: '2025',
            label: '2025'
          }, {
            value: '2026',
            label: '2026'
          }, {
            value: '2027',
            label: '2027'
          }]
        },
        form: {
          value: true,
          component: {
            span: 12,
            placeholder: '请选择年度'
          }
        }
      }
    ].concat(vm.commonEndColumns())
  }
}
