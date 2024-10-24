<template>
  <div class="container">
    <h1>{{ isEdit ? 'Atualizar Usuário' : 'Adicionar Usuário' }}</h1>

    <!-- Mensagem de erro -->
    <div v-if="errorMessage" class="alert alert-danger">
      {{ errorMessage }}
    </div>
    
    <!-- Formulário de usuário -->
    <form @submit.prevent="onSubmit">
      <!-- Campo Nome de Usuário -->
      <div class="form-group">
        <label for="user">Nome de Usuário:</label>
        <input
          type="text"
          id="user"
          v-model="form.user"
          class="form-control"
          required
          placeholder="Digite o nome de usuário"
        />
      </div>

      <!-- Campo Senha -->
      <div class="form-group">
        <label for="password">Senha:</label>
        <input
          type="password"
          id="password"
          v-model="form.password"
          class="form-control"
          required
          placeholder="Digite a senha"
        />
      </div>

      <!-- Checkbox para ativar/desativar usuário -->
      <div class="form-group form-check">
        <input
          type="checkbox"
          id="is_user_active"
          v-model="form.is_user_active"
          class="form-check-input"
        />
        <label class="form-check-label" for="is_user_active">
          Usuário Ativo
        </label>
      </div>

      <!-- Grupo de checkboxes para as funções de administrador, gerente e testador -->
      <div class="form-group">
        <label>Funções do Usuário:</label>
        
        <div class="form-check">
          <input
            type="checkbox"
            id="is_user_admin"
            v-model="form.is_user_admin"
            class="form-check-input"
          />
          <label class="form-check-label" for="is_user_admin">
            Administrador
          </label>
        </div>

        <div class="form-check">
          <input
            type="checkbox"
            id="is_user_manager"
            v-model="form.is_user_manager"
            class="form-check-input"
          />
          <label class="form-check-label" for="is_user_manager">
            Gerente
          </label>
        </div>

        <div class="form-check">
          <input
            type="checkbox"
            id="is_user_tester"
            v-model="form.is_user_tester"
            class="form-check-input"
          />
          <label class="form-check-label" for="is_user_tester">
            Testador
          </label>
        </div>
      </div>

      <!-- Botões Salvar e Cancelar -->
      <button type="submit" class="btn btn-primary">
        Salvar
      </button>
      <router-link to="/users" class="btn btn-secondary ml-2">
        Cancelar
      </router-link>
    </form>
  </div>
</template>

<script>
import userService from '../service/userService';

export default {
  name: 'UserForm',
  data() {
    return {
      past_username: '',
      form: {
        user: '',
        password: '',
        is_user_active: true,
        is_user_admin: false, 
        is_user_manager: false, 
        is_user_tester: false,
        user_timezone: ''
      },
      isEdit: false,
      errorMessage: '',
    };
  },
  methods: {
    // Método de submit do formulário
    onSubmit() {
      // Captura a timezone do navegador e adiciona ao objeto form
      this.form.user_timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

      this.errorMessage = '';
      
      if (this.isEdit) {
        userService
          .updateUser(this.form, this.past_username)
          .then(() => {
            this.$router.push('/users');
          })
          .catch((error) => {
            // Exibe a mensagem de erro se o backend retornar uma mensagem
            this.errorMessage = error.response.data.error || 'Error updating user.';
            console.error('Error updating user:', error);
          });
      } else {
        userService
          .addUser(this.form)
          .then(() => {
            this.$router.push('/users');
          })
          .catch((error) => {
            // Exibe a mensagem de erro se o backend retornar uma mensagem
            this.errorMessage = error.response.data.error || 'Error adding user.';
            console.error('Error adding user.:', error);
          });
      }
    },
  },
  // Verifica se está editando um usuário ou criando um novo
  created() {
    if (this.$route.params.user) {
      this.isEdit = true;
      userService
        .getUser(this.$route.params.user)
        .then((response) => {
          this.past_username = response.data.user;
          this.form = response.data;
        })
        .catch((error) => {
          console.error('Erro ao carregar usuário:', error);
        });
    }
  },
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin-top: 40px;
}
</style>
