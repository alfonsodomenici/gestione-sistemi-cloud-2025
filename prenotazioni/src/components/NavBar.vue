<script setup>
import {RouterLink} from 'vue-router'
import {ref} from 'vue';
import {useAuth} from '@/composables/auth';
import { useRouter } from 'vue-router';

const auth = useAuth();
const router = useRouter();

const burger = ref(null);
const nav = ref(null);

const onBurgerClick = () => {
    burger.value.classList.toggle('is-active');
    nav.value.classList.toggle('is-active');
}

const onLogout = () => {
    // Implement logout logic here, e.g., clear token, redirect to login
    console.log('User logged out');
    auth.clearToken();
    router.push('/');
}
</script>

<template>
    <nav class="navbar is-blank has-shadow is-spaced">
                <div class="navbar-brand">
            <a ref="burger" @click.prevent="onBurgerClick" role="button" class="navbar-burger" aria-label="menu"
                aria-expanded="false" data-target="navMenu">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>
        <div  ref="nav" class="navbar-menu">
            <div class="navbar-start">
                <RouterLink v-if="!auth.isAuthenticated()"  to="/" class="navbar-item">Login</RouterLink>
                <RouterLink v-if="!auth.isAuthenticated()" to="/registration" class="navbar-item">Registrati</RouterLink>
                <RouterLink v-if="auth.isAuthenticated()" to="/home" class="navbar-item">Prenotazioni</RouterLink>
                
            </div>
            <div class="navbar-end">
                <button v-if="auth.isAuthenticated()" @click.prevent="onLogout" class="button">Logout</button>
            </div>
        </div>
    </nav>
</template>