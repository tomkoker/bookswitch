<template>
  <div id='login'>
  <fieldset>
    <div class="panel-body">
      <div class="form-group">
        <input placeholder="Username" class="form-control" v-model="user.username">
      </div>
      <div class="form-group">
        <input type="password" placeholder="Password" class="form-control" v-model="user.password">
      </div>
      <div class="form-group">
        <button class="btn btn-default" v-on:click="submit">
          Log In
        </button>
      </div>
    </div>
  </fieldset>
    or <router-link to="/signup"><a>signup</a></router-link> for an account
  </div>
</template>

<script>

import axios from 'axios'
import Auth from '../auth.js'

export default {
  data: function() {
    return {
      user: {
        username: '',
        password: ''
      }
    }
  },

  methods: {
    submit: function() {
      var self = this;
      if(self.user.username && self.user.password){
          axios.post('/api/login',
            {
              username: self.user.username,
              password: self.user.password
            })
          .then(function(response){
            if(response.data.status == "success"){
              // set authenticated to true
              Auth.user.authenticated = true;

              // redirect to home
              self.$root.$router.push('/');
            } else {
              self.user.password = '';
            }
          }).catch(function(error){
            console.log(error);
          });
      }
    }
  }
}

</script>
