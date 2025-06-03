import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import RegistrationView from '@/views/RegistrationView.vue'
import ReservationsView from '@/views/ReservationsView.vue'
import CreateReservationView from '@/views/CreateReservationView.vue'

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
      path: '/reservations',
      component: ReservationsView
    },
        {
      path: '/create-reservation',
      component: CreateReservationView
    },
  ],
})

export default router
