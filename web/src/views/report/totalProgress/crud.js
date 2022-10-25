export const crudOptions = (vm) => {
  return {
    columns: [{
      title: '分部',
      key: 'section_name',
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
          value: 's4-A',
          label: '四分部A段'
        }, {
          value: 's4-B',
          label: '四分部B段'
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
      title: '日期',
      key: 'date',
      width: 160,
      search: {
        disabled: false,
        width: 400,
        component: { // 查询框组件配置，默认根据form配置生成
          name: 'el-date-picker',
          props: {
            type: 'monthrange',
            'range-separator': '至',
            'start-placeholder': '开始日期',
            'end-placeholder': '结束日期',
            format: 'yyyy-MM',
            valueFormat: 'yyyy-MM'
          }
        }
      }
    }].concat(vm.commonEndColumns())
  }
}
