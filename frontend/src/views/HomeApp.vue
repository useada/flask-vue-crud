<template>
  <div class="container">
    <h1>Welcome to the User Management System!</h1>
    <router-link to="/users" class="btn btn-primary">Manage Users</router-link>
  </div>
</template>
  
<script>
  export default {
    name: 'HomeApp',
  };
</script>
  
<style scoped>
  h1 {
    margin-top: 50px;
    text-align: center;
  }
</style>
  