 <template>
  <!-- Main Page Container -->
  <div>

    <!-- Main Header Content -->
    <div class="container-fluid">

      <!-- Header -->
      <div id="header" class="row">
        <div class="col-md-8 col-md-offset-2 col-xs-12">

          <div class="row">
            <div class="col-md-6 col-xs-8" v-once>
              <img id="logoImg" class="hidden-sm hidden-xs" src="/assets/logo.svg"/>
              <h1 id="logoText" class="hidden-sm hidden-xs"> bookflip </h1>

              <img id="logoImgSmall" class="hidden-md hidden-lg" sr="/assets/logo.svg"/>
              <h1 id="logoTextSmall" class="hidden-md hidden-lg"> bookflip </h1>
            </div>


            <!-- Fix this mess by using v-bind:class to dynamically adjust bootstrap, cleaning up redundant html -->
            <!-- Although that means the page won't adjust on the fly, it would require a reload of the page to take effect, I think... -->

            <!-- Additionally it should be possible to use a v-bind to adjust the to="/blah" parameters dynamically -->
            <!-- Used in combination with a v-text: it should be possible to consolidate these two similar blocks of code -->

            <div class="col-md-6 col-xs-4" v-if="!user.authenticated">
              <div class="row">
                <div class="col-lg-12 hidden-sm hidden-xs hidden-md">
                  <div class="btn-group accountBtn" role="group">
                    <router-link to="/login" class="btn btn-default"> Log In </router-link>
                    <router-link to="/signup" class="btn btn-default"> Sign Up </router-link>
                  </div>
                </div>
                <div class="col-xs-12 hidden-lg">
                  <div class="btn-group-vertical accountBtn" role="group">
                    <router-link to="/login" class="btn btn-default"> Log In </router-link>
                    <router-link to="/signup" class="btn btn-default"> Sign Up </router-link>
                  </div>
                </div>
              </div>
            </div>

            <div class="col-md-6 col-xs-4" v-if="user.authenticated">
              <div class="row">
                <div class="col-lg-12 hidden-sm hidden-xs hidden-md">
                  <div class="btn-group accountBtn" role="group">
                    <router-link to="/account" class="btn btn-default"> Account </router-link>
                    <button v-on:click="logout()" class="btn btn-default"> Log Out </button>
                  </div>
                </div>
                <div class="col-xs-12 hidden-lg">
                  <div class="btn-group-vertical accountBtn" role="group">
                    <router-link to="/account" class="btn btn-default"> Account </router-link>
                    <button v-on:click="logout()" class="btn btn-default"> Log Out </button>
                  </div>
                </div>
              </div>
            </div>

          </div>

        </div>
      </div>


      <!-- Navigation Bar -->
      <div id="navbar" class="row">
        <div class="col-md-8 col-md-offset-2 col-xs-12">

          <!-- In the future use a v:text here -->
          <div id="schoolName" class="col-md-9 hidden-sm hidden-xs"> Worcester Polytechnic Institute </div>
          <div id="schoolName" class="col-xs-4 hidden-md hidden-lg"> WPI </div>

          <!-- Again, using v:bind these can be consolidated -->
          <div id="transaction" class="col-md-3 col-xs-8" v-if="user.authenticated">
            <router-link to="/buy">Buy </router-link>
            |
            <router-link to="/sell">Sell </router-link>
          </div>

          <div id="transaction" class="col-md-3 col-xs-8" v-else>
            <router-link to="/buy"> Buy </router-link>
            |
            <router-link to="/login"> Sell </router-link>
          </div>

        </div>
      </div>
    </div>

    <!-- Dynamic Content -->
    <div class="container-fluid" id="dynamicContent">
      <div class="row">

        <!-- Dynamically Loaded Content -->
        <div class="col-md-8 col-md-offset-2 col-xs-12">
          <router-view></router-view>
        </div>

      </div>
    </div>

  </div>
</template>

<script>

import axios from 'axios'
import Auth from '../auth.js'

export default {
  name: 'app',
  data: function () {
    return {
      user: Auth.user
    }
  },
  methods: {
    /*checkAuth: function(){
      var self = this;
      axios.get('/api/me').then(function(response) {
        console.log(response)
        if(response.data.data.authenticated){
          Auth.user.authenticated = true
          console.log('user logged in')
        } else {
          Auth.user.authenticated = false
          console.log('user logged out')
        }
      }).catch(function(error) {
        console.log(error);
      });
    },*/
    logout: function(){
      var self = this;
      console.log(self)
      self.$router.push('/login')
      axios.get('/api/logout').then(function(response) {
        if(response.data.status == "success"){
          Auth.user.authenticated = false;
        }
      }).catch(function(error) {
        console.log(error);
      });
    }
  }

}

</script>