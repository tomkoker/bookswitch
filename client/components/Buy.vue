<template>
  <div id='buy'>

      <!-- Search Bar -->
      <div>
        <input type="text" class="form-control" id="searchBar" placeholder="Search for a book...">
      </div>

      <div v-for="(listing, index) in listings">
        <div class="panel panel-default">
          <div class="panel-heading">
            <h5>{{ listing.book.title }}</h5>
          </div>
          <div class="panel-body">
            <p>{{ listing.price }}</p>
          </div>
        </div>
      </div>

  </div>
</template>

<script>

import axios from 'axios'

export default {
  data: function() {
    return {
      listings: []
    }
  },
  mounted: function() {
    var self = this;
    axios.get('/api/all').then(function(response) {
      self.listings = response.data.data.listings
    }).catch(function(error) {
      console.log(error);
    });
  },

  methods: {

  }
}
</script>