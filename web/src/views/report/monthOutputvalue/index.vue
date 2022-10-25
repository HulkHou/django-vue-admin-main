<template>
  <d2-container :class="{ 'page-compact': crud.pageOptions.compact }">
    <div slot="header">
      <crud-search
        ref="search"
        :options="crud.searchOptions"
        @submit="handleSearch"
      />
    </div>
    <img :src="plotUrl" alt="">
  </d2-container>
</template>
<script>
import * as api from './api'
import { crudOptions } from './crud'
import { d2CrudPlus } from 'd2-crud-plus'

export default {
  name: 'monthOutputvalue',
  mixins: [d2CrudPlus.crud],
  data () {
    return {
      plotUrl: ''
    }
  },
  methods: {
    getCrudOptions () {
      // this.crud.searchOptions.form.section = 's1'
      this.crud.searchOptions.form.year = '2022'
      return crudOptions(this)
    },
    pageRequest (query) {
      console.log(query)
      return api.GetReportMonthOutputvalue(query).then(res => {
        this.plotUrl = 'data:image/png;base64,' + JSON.parse(JSON.stringify(res.data)).plot_url
      })
    }
  }
}
</script>
