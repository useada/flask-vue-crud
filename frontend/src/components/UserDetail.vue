<template>
  <div class="modal fade show" tabindex="-1" role="dialog" style="display: block;" @click.self="close">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">User Details</h5>
          <button type="button" class="close" @click="close" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <p><strong>Username:</strong> {{ user.user }}</p>
          <p><strong>Functions:</strong> {{ formatRoles(user) }}</p>
          <p><strong>Timezone:</strong> {{ user.user_timezone }}</p>
          <p><strong>Active:</strong> {{ user.active ? 'Sim' : 'Não' }}</p>
          <p><strong>Last Update:</strong> {{ formatDate(user.last_updated_at) }}</p>
          <p><strong>Created In:</strong> {{ formatDate(user.created_at) }}</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="close">Fechar</button>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
  export default {
    name: 'UserDetail',
    props: {
      user: Object,
      isVisible: Boolean,
    },
    methods: {
      close() {
        this.$emit('close');
      },
      formatRoles(user) {
        let roles = [];
        if (user.is_user_admin) roles.push('Admin');
        if (user.is_user_manager) roles.push('Manager');
        if (user.is_user_tester) roles.push('Tester');
        return roles.length ? roles.join(', ') : 'None';
      },
      formatDate(dateString) {
        const date = new Date(dateString);
        const options = { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false };
        return date.toLocaleString('pt-BR', options).replace(',', '');
      },
    },
  };
</script>
  
<style scoped>

</style>
  