import { createRouter, createWebHistory } from 'vue-router';
import HomeApp from '../views/HomeApp.vue';
import UsersIndex from '../views/UserIndex.vue';
import UserForm from '../components/UserForm.vue';

const routes = [
  {
    path: '/',
    name: 'HomeApp',
    component: HomeApp,
  },
  {
    path: '/users',
    name: 'UserIndex',
    component: UsersIndex,
  },
  {
    path: '/users/new',
    name: 'NewUser',
    component: UserForm,
  },
  {
    path: '/users/:username',
    name: 'EditUser',
    component: UserForm,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
