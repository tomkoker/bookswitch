<template>
  <div id='account'>
  	<div class="row">

      <!-- Menu Bar -->
	  <div class="col-xs-4">
	    <div class="btn-group-vertical accountBtn" role="group">
	      <router-link to="/account/overview" class="btn btn-default"> Overview </router-link>
	      <router-link to="/account/listings" class="btn btn-default"> Listings </router-link>
	      <router-link to="/account/history" class="btn btn-default"> History </router-link>
	      <router-link to="/account/options" class="btn btn-default"> Options </router-link>
	    </div>
	  </div>

	  <!-- Content -->
	  <div class="col-xs-8">
	  	<div class="row">

	  	  <!-- Dynamic Content -->
	  	  <div class="col-xs-12">
	  	  	<router-view></router-view>
	  	  </div>


	  	</div>
	  </div>

	</div>
  </div>
</template>

<script>
</script>
