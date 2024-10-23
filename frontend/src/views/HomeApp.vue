<template>
    <div class="container">
      <h1>Bem-vindo ao Sistema de Gerenciamento de Usuários!</h1>
      <router-link to="/users" class="btn btn-primary">Gerenciar Usuários</router-link>
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
  