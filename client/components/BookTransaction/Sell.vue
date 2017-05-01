<template>
  <div>
    <div class="panel panel-default">
      <div class="panel-heading">
        <h3>New Listing</h3>
      </div>
      <div class="panel-body">
        <div class="form-group">
          <input class="form-control" placeholder="ISBN" v-model="listing.book.isbn">
        </div>
        <button class="btn btn-primary" v-on:click="getInfo">Next</button>
        <br>
        <br>
        <div class="form-group">
          <input placeholder="Title" class="form-control" v-model="listing.book.title" disabled>
        </div>
        <div class="form-group">
          <input placeholder="Author" class="form-control" v-model="listing.book.author" disabled>
        </div>
        <div class="form-group">
          <select placeholder="Condition" class="form-control" v-model="listing.condition">
            <option value="" disabled selected>Condition</option>
            <option>New</option>
            <option>Used (Like New)</option>
            <option>Used</option>
            <option>Poor</option>
          </select>
        </div>
        <div class="form-group">
          <input type="number" placeholder="Price" class="form-control" v-model="listing.price">
        </div>
        <button class="btn btn-primary" v-on:click="submit">Submit</button>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  data: function() {
    return {
      listing: {
        book: {
          isbn:'',
          title:'',
          author:''
        },
        condition:'',
        price:''
      }
    }
  },

  methods: {
    submit: function() {
      console.log(this.listing.book.isbn)
      var self = this;
      var listing = this.listing;
      if(listing.book.isbn && listing.book.title && listing.condition &&
        listing.book.author && listing.price){
          axios.post('/api/new-listing', {listing: listing}).then(function(response){
            console.log(response);
            self.listing = {
              book: {
                isbn:'',
                title:'',
                author:''
              },
              condition:'',
              price:''
            }
          }).catch(function(error){
            console.log(error);
          });
      }
    },
    getInfo: function() {
      console.log(this.listing.book.isbn);
      var isbn = this.listing.book.isbn.replace(/\D/g,'');
      console.log(isbn)
      var url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn;
      console.log(url)
      var self = this;
      axios.get(url).then(function(response) {
        if(response.data.totalItems){
          self.listing.book.title = response.data.items[0]["volumeInfo"]["title"];
          self.listing.book.author = response.data.items[0]["volumeInfo"]["authors"].join(', ');
        }
      }).catch(function(err) {
        console.log(err);
      });
    }
  }
}

</script>
