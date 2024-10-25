<template>
    <div class="container">
      <h1>User List</h1>
      <UserList />
      <router-link to="/users/new" class="btn btn-success">Add User</router-link>
    </div>
  </template>
  
  <script>
  import UserList from '@/components/UserList.vue';
  
  export default {
    name: 'UserIndex',
    components: {
      UserList,
    },
  };
  </script>
  