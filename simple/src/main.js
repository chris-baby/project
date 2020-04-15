import Vue from 'vue'
import VueRouter from 'vue-router'
import layout from './layout.vue'
import IndexPage from './pages/index.vue'


Vue.use(VueRouter)
let router = new VueRouter({
  mode:'history',
  routes:[
    {
      path:'/',
      component:IndexPage
    }
  ]
})
new Vue({
  el: '#app',
  router,
  components:{
    layout
  },
  template: '<layout/>'
})
