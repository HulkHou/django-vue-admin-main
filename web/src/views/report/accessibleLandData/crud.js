export const crudOptions = (vm) => {
  return {
    pageOptions: {
      compact: true
    },
    options: {
      tableType: 'vxe-table',
      stripe: false,
      rowKey: true, // 必须设置，true or false
      rowId: 'id',
      height: '100%', // 表格高度100%, 使用toolbar必须设置
      highlightCurrentRow: false,
      defaultExpandAll: true
    },
    rowHandle: {
      width: 140,
      view: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Retrieve')
        }
      },
      edit: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Update')
        }
      },
      remove: {
        thin: true,
        text: '',
        disabled () {
          return !vm.hasPermissions('Delete')
        }
      }
    },
    indexRow: {
      // 或者直接传true,不显示title，不居中
      title: '序号',
      align: 'center',
      width: 100
    },

    viewOptions: {
      componentType: 'form'
    },
    formOptions: {
      defaultSpan: 12 // 默认的表单 span
    },
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
            value: 'C1',
            label: 'C1段'
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
        title: '土地编号',
        align: 'center',
        key: 'land_code',
        sortable: true,
        search: {
          disabled: false
        },
        width: 160,
        form: {
          value: '0',
          rules: [// 表单校验规则
            {
              required: true,
              message: '土地编号必填项'
            }],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: '土地编号'
          }
        }
      }, {
        title: '土地状态',
        align: 'center',
        key: 'status',
        sortable: true,
        search: {
          disabled: false
        },
        width: 100,
        type: 'select',
        dict: {
          data: [{
            value: '1',
            label: '已交付土地'
          }, {
            value: '2',
            label: '先租后征土地'
          }, {
            value: '3',
            label: '未交付土地'
          }]
        },
        form: {
          value: '',
          rules: [// 表单校验规则
            {
              required: true,
              message: '土地状态必填项'
            }],
          component: {
            span: 8,
            placeholder: '请选择土地状态'
          }
        }
      }
    ].concat(vm.commonEndColumns())
  }
}
