<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const regForm = ref(null);
const user = ref({
    nome: '',
    cognome: '',
    tel: '',
    mail: '',
    pwd: ''
});


const onRegistration = (e) => {

    if (regForm.value.checkValidity() === false) {
        regForm.value.reportValidity();
        console.log('Form registration is invalid');
        return;
    }

    console.log('Registration attempt with:',
        user.value.nome, user.value.cognome, user.value.tel,
        user.value.mail, user.value.pwd);

    const data = {
        firstname: user.value.nome,
        lastname: user.value.cognome,
        phone: user.value.tel,
        mail: user.value.mail,
        pwd: user.value.pwd
    }
    
    fetch("http://localhost:5000/registration", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(json => console.log(json))
    router.push('/'); // Redirect to login after registration

}
</script>

<template>
    <div class="columns is-centered mt-5">
        <form ref="regForm" class="box column is-half">
            <p class="title has-text-centered">Registrati</p>
            <div class="field">
                <label class="label">Nome</label>
                <div class="control">
                    <input v-model="user.nome" class="input" type="text" name="nome" id="nome" required>
                </div>
            </div>
            <div class="field">
                <label class="label">Cognome</label>
                <div class="control">
                    <input v-model="user.cognome" class="input" type="text" name="cognome" id="cognome" required>
                </div>
            </div>
            <div class="field">
                <label class="label">Tel</label>
                <div class="control">
                    <input v-model="user.tel" class="input" type="tel" name="tel" id="tel">
                </div>
            </div>
            <div class="field">
                <label class="label">Email</label>
                <div class="control">
                    <input v-model="user.mail" class="input" type="email" name="email" id="email" required>
                </div>
            </div>
            <div class="field">
                <label class="label">Password</label>
                <div class="control">
                    <input v-model="user.pwd" class="input" type="password" name="pwd" id="pwd" required>
                </div>
            </div>
            <div class="field">
                <button @click.prevent="onRegistration" class="button is-primary">Registrati</button>
            </div>
        </form>
    </div>
</template>