<template>
    <div>
      <table class="table">
        <thead>
          <tr>
            <th>Nome de Usuário</th>
            <th>Ativo</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.username">
            <td>{{ user.username }}</td>
            <td>{{ user.active ? 'Sim' : 'Não' }}</td>
            <td>
              <router-link :to="{ name: 'EditUser', params: { username: user.username } }" class="btn btn-info btn-sm">Editar</router-link>
              <button @click="deleteUser(user.username)" class="btn btn-danger btn-sm">Excluir</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import userService from '../service/userService';
  
  export default {
    name: 'UserList',
    data() {
      return {
        users: [],
      };
    },
    methods: {
      fetchUsers() {
        userService.getUsers()
          .then(response => {
            this.users = response.data;
          })
          .catch(error => {
            console.error('Erro ao buscar usuários:', error);
          });
      },
      deleteUser(username) {
        userService.deleteUser(username)
          .then(() => {
            this.fetchUsers();
          })
          .catch(error => {
            console.error('Erro ao deletar usuário:', error);
          });
      },
    },
    created() {
      this.fetchUsers();
    },
  };
  </script>
  