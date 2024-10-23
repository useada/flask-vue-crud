<template>
    <div class="container">
      <h1>Lista de Usuários</h1>
      <UserList />
      <router-link to="/users/new" class="btn btn-success">Adicionar Usuário</router-link>
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
  