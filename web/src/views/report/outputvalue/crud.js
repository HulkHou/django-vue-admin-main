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
        title: 'ID',
        key: 'id',
        show: false,
        disabled: true,
        width: 90,
        form: {
          disabled: true
        }
      },
      {
        title: '分部名称',
        align: 'center',
        key: 'section_name',
        sortable: true,
        search: {
          disabled: false
        },
        width: 100,
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
          value: 's1',
          rules: [
            // 表单校验规则
            {
              required: true,
              message: '分部名称必填项'
            }
          ],
          component: {
            span: 8,
            placeholder: '请选择分部'
          }
        }
      },
      {
        title: '年度',
        align: 'center',
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
          value: '2022',
          rules: [
            // 表单校验规则
            {
              required: true,
              message: '年度必填项'
            }
          ],
          component: {
            span: 8,
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
          value: '1',
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
      },
      {
        title: '月度产值-保底计划',
        align: 'center',
        key: 'output_value_lowest',
        sortable: true,
        width: 160,
        form: {
          value: '0',
          rules: [
            // 表单校验规则
            {
              required: true,
              message: '月度产值-保底计划必填项'
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: '月度产值-保底计划'
          }
        }
      },
      {
        title: '月度产值-力争计划',
        align: 'center',
        key: 'output_value_target',
        sortable: true,
        width: 160,
        form: {
          value: '0',
          rules: [
            // 表单校验规则
            {
              required: true,
              message: '月度产值-力争计划必填项'
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: '月度产值-力争计划'
          }
        }
      },
      {
        title: '月度产值-实际',
        align: 'center',
        key: 'output_value_actual',
        sortable: true,
        width: 160,
        form: {
          value: '0',
          rules: [
            // 表单校验规则
            {
              required: true,
              message: '月度产值-实际必填项'
            }
          ],
          component: {
            span: 12,
            props: {
              clearable: true
            },
            placeholder: '月度产值-实际'
          }
        }
      }
    ].concat(vm.commonEndColumns())
  }
}
