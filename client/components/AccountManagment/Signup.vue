<template>
  <div>
    <fieldset>
    <div class="panel-body">
      <div class="form-group">
        <input placeholder="Username" class="form-control" v-model="user.username">
      </div>
      <div class="form-group">
        <input placeholder="Email" class="form-control" v-model="user.email">
      </div>
      <div class="form-group">
        <input type="password" placeholder="Password" class="form-control" v-model="user.password">
      </div>
      <div class="form-group">
        <button class="btn btn-default" v-on:click="submit">
          Signup
        </button>
      </div>
    </div>
    </fieldset>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  data: function() {
    return {
      user: {
        username: '',
        email: '',
        password: ''
      }
    }
  },

  methods: {
    submit: function() {
      var self = this;
      if(self.user.email && self.user.password){
          axios.post('/api/signup', {
              username: self.user.username,
              email: self.user.email,
              password: self.user.password
            })
          .then(function(response){
            console.log(response);
            self.user.username = '';
            self.user.email = '';
            self.user.password = '';
          }).catch(function(error){
            console.log(error);
          });
      }
    }
  }
}

</script>