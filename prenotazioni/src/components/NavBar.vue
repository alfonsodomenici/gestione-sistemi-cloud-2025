<script setup>
import {RouterLink} from 'vue-router'

</script>

<template>
    <nav class="navbar is-blank has-shadow is-spaced">
        <div class="navbar-menu">
            <div class="navbar-start">
                <RouterLink to="/" class="navbar-item">Login</RouterLink>
                <RouterLink to="/registration" class="navbar-item">Registrati</RouterLink>
            </div>
        </div>
    </nav>
</template>