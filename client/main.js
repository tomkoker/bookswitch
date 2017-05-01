import Vue from 'vue'
import VueRouter from 'vue-router'

// Main Web Components
import App from './components/App.vue'
import Splash from './components/Splash.vue'

// General UI Elements and Pages
import Home from './components/GeneralUI/Home.vue'

// Book Buy, Sell and sub pages
import Buy from './components/BookTransaction/Buy.vue'
import Sell from './components/BookTransaction/Sell.vue'

// Specific pages for user account managment and interface.
import Login from './components/AccountManagment/Login.vue'
import Signup from './components/AccountManagment/Signup.vue'

// School Dependent Modifications
// import WPI from './component/Schools/WorcesterPolytechnicInstitute.vue'

Vue.use(VueRouter)

let router = new VueRouter({
  routes: [
    { path: '/', component: App},
    { path: '/buy', component: Buy},
    { path: '/sell', component: Sell},
    { path: '/login', component: Login},
    { path: '/signup', component: Signup},
    { path: '/home', component: Home}
  ]
})

new Vue({ // eslint-disable-line no-new
  el: '#app',
  router,
  render: h => h(App)
})
