<script setup>
import { ref } from 'vue';
import { useAuth } from '@/composables/auth';

const prenotazioni = ref([]);

fetch(`http://localhost:5000/prenotazioni/${useAuth().getToken().id}`, {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
    }
})
.then(response => response.json())
.then(data => {
    prenotazioni.value = data;
})
.catch(error => {
    console.error("Error fetching reservations:", error);
});




</script>

<template>
    <div class="columns is-centered mt-5">
        <div class="box column is-half">
            <p class="title has-text-centered">Benvenuto nella pagina delle tue prenotazioni</p>
            <ul>
                <li v-for="prenotazione in prenotazioni" :key="prenotazione.id">
                    {{ prenotazione.id }}
                {{ prenotazione.tipo }}
                {{ prenotazione.costo }}
                {{ prenotazione.datavisita }}
                </li>
            </ul>
        </div>
    </div>
</template>