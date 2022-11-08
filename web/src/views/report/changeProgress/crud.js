export const crudOptions = (vm) => {
  return {
    columns: [
      {
        title: '土地分段',
        align: 'center',
        key: 'land_section',
        sortable: true,
        search: {
          disabled: false
        },
        width: 100,
        type: 'select',
        dict: {
          data: [{
            value: 'A',
            label: 'A段'
          }, {
            value: 'B',
            label: 'B段'
          }, {
            value: 'C1A',
            label: 'C1A段'
          }, {
            value: 'C2',
            label: 'C2段'
          }]
        },
        form: {
          value: '',
          rules: [// 表单校验规则
            {
              required: true,
              message: '土地分段必填项'
            }],
          component: {
            span: 8,
            placeholder: '请选择土地分段'
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
            value: '2022',
            label: '2022'
          }, {
            value: '2023',
            label: '2023'
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
