import Vue from 'vue'
import App from './App.vue'
import router from './routes'
import store from './store'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.config.productionTip = false

import 'bootstrap/dist/css/bootstrap.css' 
import 'bootstrap-vue/dist/bootstrap-vue.css' 

Vue.use(BootstrapVue)
Vue.use(IconsPlugin) 



new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
