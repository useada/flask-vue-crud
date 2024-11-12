import { createRouter, createWebHistory } from 'vue-router';
import HomeApp from '../views/HomeApp.vue';
import ChartApp from '../views/ChartApp.vue';
import UsersIndex from '../views/UserIndex.vue';
import UserForm from '../components/UserForm.vue';
import UserDetail from '../components/UserDetail.vue';


const routes = [
  {
    path: '/',
    name: 'HomeApp',
    component: HomeApp,
  },
  {
    path: '/chart',
    name: 'ChartApp',
    component: ChartApp,
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
    path: '/users/:user',
    name: 'EditUser',
    component: UserForm,
  },
  {
    path: '/user-detail/:username',
    name: 'UserDetail',
    component: UserDetail,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
