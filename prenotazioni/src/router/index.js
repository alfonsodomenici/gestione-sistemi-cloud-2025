import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import RegistrationView from '@/views/RegistrationView.vue'
import HomeView from '@/views/HomeView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: LoginView
    },
    {
      path: '/registration',
      component: RegistrationView
    },
    {
      path: '/home',
      component: HomeView
    },
  ],
})

export default router
