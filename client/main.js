import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './components/App.vue'

import Buy from './components/Buy.vue'
import Sell from './components/Sell.vue'
import Login from './components/Login.vue'
import Signup from './components/Signup.vue'
import Account from './components/Account.vue'

import AccountGreeting from './components/account/Greeting.vue'
import AccountOverview from './components/account/Overview.vue'
import AccountListings from './components/account/Listings.vue'
import AccountHistory from './components/account/History.vue'
import AccountOptions from './components/account/Options.vue'

import Auth from './auth.js'

Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    { path: '/', component: Buy},
    { path: '/buy', component: Buy},
    { path: '/sell', component: Sell, meta: {auth: true}},
    { path: '/login', component: Login},
    { path: '/signup', component: Signup},
    { path: '/account', component: Account,
      children: [
        { path: '', component: AccountGreeting},
        { path: 'overview', component: AccountOverview},
        { path: 'listings', component: AccountListings},
        { path: 'history', component: AccountHistory},
        { path: 'options', component: AccountOptions}
        ]}
  ]
})

router.beforeEach((to, from, next) => {
  Auth.checkAuth()
  .then(function() {

    if(to.meta.auth && !Auth.user.authenticated){
      return next({path: '/login'})
    }
    return next()
  })
  .catch(error => {
    console.log(error)
    return next()
  })
})

new Vue({ // eslint-disable-line no-new
  el: '#app',
  router,
  render: h => h(App)
})