<script setup>
import {RouterLink} from 'vue-router'
import {ref} from 'vue';

const burger = ref(null);
const nav = ref(null);

const onBurgerClick = () => {
    burger.value.classList.toggle('is-active');
    nav.value.classList.toggle('is-active');
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
                <RouterLink to="/" class="navbar-item">Login</RouterLink>
                <RouterLink to="/registration" class="navbar-item">Registrati</RouterLink>
            </div>
        </div>
    </nav>
</template>