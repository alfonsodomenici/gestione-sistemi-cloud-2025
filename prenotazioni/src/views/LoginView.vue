<script setup>
import { ref } from 'vue';
import { useAuth } from '@/composables/auth';
import { useRouter } from 'vue-router';

const auth = useAuth();
const router = useRouter();

const formLogin = ref(null);
const credential = ref({
    mail: '',
    pwd: ''
});


const onLogin = (e) => {
    console.log('User authenticated:', auth.isAuthenticated());

    if (formLogin.value.checkValidity() === false) {
        formLogin.value.reportValidity();
        console.log('Form login is invalid');
        return;
    }
    console.log('Login attempt with:',
        credential.value.mail, credential.value.pwd);

    const data = {
        mail: credential.value.mail,
        pwd: credential.value.pwd
    }

    fetch("http://localhost:5000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
        .then(response => {
            if (!response.ok) {
                alert('Login failed: ' + response.statusText);
                throw new Error('Login failed');
            }
            return response.json();
        })
        .then(json => {
            console.log('Login successful:', json);
            auth.setToken(json);
            console.log('User authenticated:', auth.isAuthenticated());
            router.push('/reservations');
        })
        .catch(error => {
            console.error('Error during login:', error);
        });



}



</script>

<template>
    <div class="columns is-centered mt-5">
        <form ref="formLogin" class="box column is-half">
            <p class="title has-text-centered">Login</p>
            <div class="field">
                <label class="label">Email</label>
                <div class="control">
                    <input v-model="credential.mail" class="input" type="email" name="email" id="email" required>
                </div>
            </div>
            <div class="field">
                <label class="label">Password</label>
                <div class="control">
                    <input v-model="credential.pwd" class="input" type="password" name="pwd" id="pwd" required>
                </div>
            </div>
            <div class="field">
                <button @click.prevent="onLogin" class="button is-primary">Login</button>
            </div>
        </form>
    </div>
</template>