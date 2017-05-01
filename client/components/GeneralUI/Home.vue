<template>
  <!-- Main Page Container -->
  <div class="container" id="app">

  <!-- Left Hand Side Bar -->
  <div class="col-sm-2">
  <p> filler text </p>
  </div>

  <!-- Main (Center) Content -->
  <div class="col-sm-8">

    <!-- Header -->
    <div class="page-header" id="header"> 
      <img id="logoImg" src="/assets/logo.svg"/>
      <h1 id="logoText">bookflip</h1> 
    </div>

    <!-- Navigation Bar -->
    <div class="page-header" id="navbar">
      <span> </span>
      <span> </span>
      <span> </span>
    
    </div>

    <!-- REPLACE -->
    <div>
      <router-link v-show="!authenticated" to="/login" > <a>Login</a> </router-link>
      <router-link v-show="!authenticated" to="/signup" > <a>Signup</a> </router-link>

      <a v-show="authenticated" v-on:click="logout" href="#">Logout</a>
    </div>

    
    <div>
      <ul class="nav nav-tabs">
        <router-link tag="li" to="/buy" active-class="active"> <a>Buy</a> </router-link>
        <router-link tag="li" to="/sell" active-class="active"> <a>Sell</a> </router-link>
      </ul>
    </div>
    <!-- end REPLACE -->


    <!-- Dynamicaly Loaded Content -->
    <div>
      <br>
      <router-view></router-view>
    </div>

  </div>

  <!-- Right Hand Side Bar -->
  <div class="col-sm-2">
  </div>

  </div>
</template>


<script>

import axios from 'axios'

export default {
  name: 'app',
  data: function () {
    return {
      authenticated: false
    }
  },
  methods: {
    checkAuth: function(){
      var self = this;
      axios.get('/api/me').then(function(response) {
        if(response.data.status == "LoggedIn"){
          self.authenticated = true;
        }
      }).catch(function(error) {
        console.log(error);
      });
    },
    logout: function(){
      var self = this;
      axios.get('/api/logout').then(function(response) {
        if(response.data.status == "success"){
          self.authenticated = false;
        }
      }).catch(function(error) {
        console.log(error);
      });
    }
  },
  beforeMount: function(){
    this.checkAuth();
  },
}
</script>

