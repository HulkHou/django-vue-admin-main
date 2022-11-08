export const crudOptions = (vm) => {
  return {
    columns: [{
      title: '标段',
      key: 'land_section',
      sortable: true,
      search: {
        disabled: false
      },
      width: 90,
      type: 'select',
      dict: {
        data: [{
          value: 'CH0-45',
          label: 'CH0-45'
        }, {
          value: 'CH45-120',
          label: 'CH45-120'
        }, {
          value: 'CH120-215',
          label: 'CH120-215'
        }, {
          value: 'CH215-325',
          label: 'CH215-325'
        }, {
          value: 'CH325-426',
          label: 'CH325-426'
        }, {
          value: 'CH426-508',
          label: 'CH426-508'
        }, {
          value: 'CH508-523',
          label: 'CH508-523'
        }]
      },
      form: {
        value: true,
        component: {
          span: 12,
          placeholder: '请选择标段'
        }
      }
    }].concat(vm.commonEndColumns())
  }
}
