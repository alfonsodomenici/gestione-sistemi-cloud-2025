<script setup>
import { ref } from 'vue';

const formLogin = ref(null);
const credential = ref({
    mail: '',
    pwd: ''
});


const onLogin = (e) => {
    console.log(formLogin.value.checkValidity())
    if(formLogin.value.checkValidity() === false) {
        formLogin.value.reportValidity();
        console.log('Form login is invalid');
        return;
    }
    console.log('Login attempt with:', 
        credential.value.mail, credential.value.pwd);
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