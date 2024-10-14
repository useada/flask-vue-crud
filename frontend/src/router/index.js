import { createRouter, createWebHistory } from "vue-router";
import Test from "../components/TestItem.vue";

const routes = [
  {
    path: "/testItem",
    name: "TestItem",
    component: Test,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
