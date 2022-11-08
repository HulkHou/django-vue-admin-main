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
          value: '',
          rules: [
            // 表单校验规则
            {
              required: true,
              message: '年度必填项'
            }
          ],
          component: {
            span: 12,
            placeholder: '请选择年度'
          }
        }
      },
      {
        title: '月份',
        align: 'center',
        key: 'month',
        sortable: true,
        search: {
          disabled: false
        },
        width: 90,
        type: 'select',
        dict: {
          data: [{
            value: '1',
            label: '1'
          }, {
            value: '2',
            label: '2'
          }, {
            value: '3',
            label: '3'
          }, {
            value: '4',
            label: '4'
          }, {
            value: '5',
            label: '5'
          }, {
            value: '6',
            label: '6'
          }, {
            value: '7',
            label: '7'
          }, {
            value: '8',
            label: '8'
          }, {
            value: '9',
            label: '9'
          }, {
            value: '10',
            label: '10'
          }, {
            value: '11',
            label: '11'
          }, {
            value: '12',
            label: '12'
          }]
        },
        form: {
          value: '',
          rules: [
            // 表单校验规则
            {
              required: true,
              message: '月份必填项'
            }
          ],
          component: {
            span: 8,
            placeholder: '请选择月份'
          }
        }
      }, {
        title: '迁改计划值',
        align: 'center',
        key: 'change_progress_target',
        sortable: true,
        width: 160,
        form: {
          value: '0',
          rules: [// 表单校验规则
            {
              required: true,
              message: '迁改计划值必填项'
            }],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: '迁改计划值'
          }
        }
      }, {
        title: '迁改实际值',
        align: 'center',
        key: 'change_progress_actual',
        sortable: true,
        width: 160,
        form: {
          value: '0',
          rules: [// 表单校验规则
            {
              required: true,
              message: '迁改实际值必填项'
            }],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: '迁改实际值'
          }
        }
      }, {
        title: '迁改预计值',
        align: 'center',
        key: 'change_progress_predict',
        sortable: true,
        width: 160,
        form: {
          value: '0',
          rules: [// 表单校验规则
            {
              required: true,
              message: '迁改预计值必填项'
            }],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: '迁改预计值'
          }
        }
      }
    ].concat(vm.commonEndColumns())
  }
}
