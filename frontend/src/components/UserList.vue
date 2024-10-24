<template>
    <div>
      <table class="table">
        <thead>
          <tr>
            <th>Username</th>
            <th>Roles</th>
            <th>Timezone</th>
            <th>Active</th>
            <th>Last Updated At</th>
            <th>Created At</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.user">
            <td>{{ user.user }}</td>
            <td>{{ formatRoles(user) }}</td>
            <td>{{ user.user_timezone }}</td>
            <td>{{ user.active ? 'Yes' : 'No' }}</td>
            <td>{{ formatDate(user.last_updated_at) }}</td>
            <td>{{ formatDate(user.created_at) }}</td>
            <td>
              <router-link :to="{ name: 'EditUser', params: { user: user.user } }" class="btn btn-info btn-sm">Editar</router-link>
              <button @click="deleteUser(user.user)" class="btn btn-danger btn-sm">Excluir</button>
              <button @click="showDetail(user)" class="btn btn-secondary btn-sm">Detalhar</button>
            </td>
          </tr>
        </tbody>
      </table>
      <UserDetail 
        v-if="selectedUser" 
        :user="selectedUser" 
        :isVisible="!!selectedUser" 
        @close="selectedUser = null" 
      />
    </div>

    
  </template>
  
  <script>
  import userService from '../service/userService';
  import UserDetail from '../components/UserDetail.vue';
  
  export default {
    name: 'UserList',
    components: {
      UserDetail
    },
    data() {
      return {
        users: [],
        selectedUser: null,
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
      deleteUser(user) {
        userService.deleteUser(user)
          .then(() => {
            this.fetchUsers();
          })
          .catch(error => {
            console.error('Erro ao deletar usuário:', error);
          });
      },
      showDetail(user) {
        this.selectedUser = user; // Define o usuário selecionado
      },
      formatRoles(user) {
        let roles = [];
        if (user.is_user_admin) roles.push('Admin');
        if (user.is_user_manager) roles.push('Manager');
        if (user.is_user_tester) roles.push('Tester');
        return roles.length ? roles.join(', ') : 'Nenhum'; 
      },
      formatDate(dateString) {
      const date = new Date(dateString);
      const options = { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false };
      return date.toLocaleString('pt-BR', options).replace(',', '');
    },
    },
    created() {
      this.fetchUsers();
    },
  };
  </script>
  