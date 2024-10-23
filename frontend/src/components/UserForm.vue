<template>
    <div class="container">
      <h1>{{ isEdit ? 'Atualizar Usuário' : 'Adicionar Usuário' }}</h1>
      <b-form @submit.prevent="onSubmit">
        <b-form-group label="Nome de Usuário:" label-for="username">
          <b-form-input
            id="username"
            v-model="form.username"
            required
            placeholder="Digite o nome de usuário"
          ></b-form-input>
        </b-form-group>
  
        <b-form-group label="Senha:" label-for="password">
          <b-form-input
            id="password"
            type="password"
            v-model="form.password"
            required
            placeholder="Digite a senha"
          ></b-form-input>
        </b-form-group>
  
        <b-button type="submit" variant="primary">Salvar</b-button>
        <router-link to="/users" class="btn btn-secondary">Cancelar</router-link>
      </b-form>
    </div>
  </template>
  
  <script>
  import userService from '../service/userService';
  
  export default {
    name: 'UserForm',
    data() {
      return {
        form: {
          username: '',
          password: '',
        },
        isEdit: false,
      };
    },
    methods: {
      onSubmit() {
        if (this.isEdit) {
          userService.updateUser(this.form.username, this.form)
            .then(() => {
              this.$router.push('/users');
            })
            .catch(error => {
              console.error('Erro ao atualizar usuário:', error);
            });
        } else {
          userService.addUser(this.form)
            .then(() => {
              this.$router.push('/users');
            })
            .catch(error => {
              console.error('Erro ao adicionar usuário:', error);
            });
        }
      },
    },
    created() {
      if (this.$route.params.username) {
        this.isEdit = true;
        userService.getUser(this.$route.params.username)
          .then(response => {
            this.form = response.data;
          })
          .catch(error => {
            console.error('Erro ao carregar usuário:', error);
          });
      }
    },
  };
  </script>
  