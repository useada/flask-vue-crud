<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/flatly/bootstrap.min.css"
        integrity="sha384-qF/QmIAj5ZaYFAeQcrQ6bfVMAh4zZlrGwTPY7T/M+iTTLJqJBJjwwnsE5Y0mV7QK"
        crossorigin="anonymous"
      />
      <div class="row">
        <div class="col-sm-12">
          <h1 class="text-center bg-primary text-white" style="border-radius: 10px;">Users</h1>
          <hr />
          <br />

          <!-- Alert message -->

          <button type="button" class="btn btn-success">Add User</button>
          <br />
          <br />
          <table class="table table-hover">
            <!-- Table Head -->
            <thead>
              <tr>
                <th scope="col">Username</th>
                <th scope="col">Roles</th>
                <th scope="col">Timezone</th>
                <th scope="col">Is Active?</th>
                <th scope="col">Last Updated At</th>
                <th scope="col">Created At</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="user, index in users" :key="index">
                <td>{{ user.username }}</td>
                <td>{{ user.roles }}</td>
                <td>{{ user.timezone }}</td>
                <td>
                  <span v-if="user.is_active">Yes</span>
                  <span v-else>No</span>
                </td>
                <td>{{ user.updated_ts }}</td>
                <td>{{ user.created_ts }}</td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-info btn-sm">
                      Update
                    </button>
                    <button type="button" class="btn btn-danger btn-sm">
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UsersIndex",
  props: {
    users: [],
  },
};
</script>
