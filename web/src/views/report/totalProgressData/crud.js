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
    columns: [{
      title: 'ID',
      key: 'id',
      show: false,
      disabled: true,
      width: 90,
      form: {
        disabled: true
      }
    }, {
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
        value: 's1',
        rules: [// 表单校验规则
          {
            required: true,
            message: '分部名称必填项'
          }],
        component: {
          span: 8,
          placeholder: '请选择分部'
        }
      }
    }, {
      title: '日期',
      align: 'center',
      key: 'date',
      width: 160,
      type: 'date',
      search: {
        disabled: false,
        component: { // 查询框组件配置，默认根据form配置生成
          props: {
            placeholder: '请选择日期',
            type: 'month',
            valueFormat: 'yyyy-MM'
          }
        }
      },
      form: {
        disabled: false,
        rules: [// 表单校验规则
          {
            required: true,
            message: '日期必填项'
          }],
        component: { // 查询框组件配置，默认根据form配置生成
          props: {
            placeholder: '请选择日期',
            type: 'month',
            valueFormat: 'yyyy-MM'
          }
        }
      }
    }, {
      title: '工期进度线',
      align: 'center',
      key: 'total_progress',
      sortable: true,
      width: 160,
      form: {
        value: '0',
        rules: [// 表单校验规则
          {
            required: true,
            message: '工期进度线必填项'
          }],
        component: {
          span: 12,
          props: {
            clearable: true
          },
          placeholder: '工期进度线'
        }
      }
    }, {
      title: '月度计划',
      align: 'center',
      key: 'month_progress_target',
      sortable: true,
      width: 160,
      form: {
        value: '0',
        rules: [// 表单校验规则
          {
            required: true,
            message: '月度计划必填项'
          }],
        component: {
          span: 12,
          props: {
            clearable: true
          },
          placeholder: '月度计划'
        }
      }
    }, {
      title: '月度完成',
      align: 'center',
      key: 'month_progress_actual',
      sortable: true,
      width: 160,
      form: {
        value: '0',
        rules: [// 表单校验规则
          {
            required: true,
            message: '月度完成必填项'
          }],
        component: {
          span: 12,
          props: {
            clearable: true
          },
          placeholder: '月度完成'
        }
      }
    }].concat(vm.commonEndColumns())
  }
}
