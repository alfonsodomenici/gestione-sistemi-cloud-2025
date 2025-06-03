<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'

</script>

<template>
  <NavBar />  
  <div class="container is-fluid pt-4 pb-4 is-half">
    <RouterView />
  </div>

</template>
