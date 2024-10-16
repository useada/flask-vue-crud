import { createRouter, createWebHistory } from "vue-router";
import Users from "../components/UsersIndex.vue";

const routes = [
  {
    path: "/users",
    name: "Users",
    component: Users,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
