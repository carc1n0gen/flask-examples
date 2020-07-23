import Vue from 'vue';
import VueRouter from 'vue-router';
import { BootstrapVue } from 'bootstrap-vue'
import App from './App.vue';
import { Home, Person, About, NotFound } from './pages';

Vue.use(VueRouter);
Vue.use(BootstrapVue);

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About },
    { path: '/user/:id', component: Person },
    { path: '*', component: NotFound }
  ]
})

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
});
