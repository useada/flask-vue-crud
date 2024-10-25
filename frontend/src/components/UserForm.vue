<template>
  <div class="container">
    <h1>{{ isEdit ? 'Update User' : 'Add User' }}</h1>

    <!-- Error message -->
    <div v-if="errorMessage" class="alert alert-danger">
      {{ errorMessage }}
    </div>
    
    <!-- Userform -->
    <form @submit.prevent="onSubmit">
      <!-- Username field -->
      <div class="form-group">
        <label for="user">Username:</label>
        <input
          type="text"
          id="user"
          v-model="form.user"
          class="form-control"
          required
          placeholder="Enter username"
        />
      </div>

      <!-- Password field -->
      <div class="form-group">
        <label for="password">Password:</label>
        <input
          type="password"
          id="password"
          v-model="form.password"
          class="form-control"
          required
          placeholder="Enter password"
        />
      </div>

      <!-- Checkbox to activate/deactivate user -->
      <div class="form-group form-check">
        <input
          type="checkbox"
          id="is_user_active"
          v-model="form.is_user_active"
          class="form-check-input"
        />
        <label class="form-check-label" for="is_user_active">
          Active User
        </label>
      </div>

      <!-- Group of checkboxes for administrator, manager and tester roles -->
      <div class="form-group">
        <label>User Roles:</label>
        
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
            Manager
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
            Tester
          </label>
        </div>
      </div>

      <!-- Save and Cancel buttons -->
      <button type="submit" class="btn btn-primary">
        Save
      </button>
      <router-link to="/users" class="btn btn-secondary ml-2">
        Cancel
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
    onSubmit() {
      // Captures the browser timezone and adds it to the form object
      this.form.user_timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

      this.errorMessage = '';
      
      if (this.isEdit) {
        userService
          .updateUser(this.form, this.past_username)
          .then(() => {
            this.$router.push('/users');
          })
          .catch((error) => {
            // Display the error message if the backend returns a message
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
            // Display the error message if the backend returns a message
            this.errorMessage = error.response.data.error || 'Error adding user.';
            console.error('Error adding user.:', error);
          });
      }
    },
  },
  // Checks whether you are editing a user or creating a new one
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
