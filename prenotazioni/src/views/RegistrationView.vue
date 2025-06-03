<script setup>

const onRegistration = (e) => {
    console.log('effettuare registrazione')
}
</script>

<template>
    <div class="columns is-centered mt-5">
        <form class="box column is-half">
            <p class="title has-text-centered">Registrati</p>
            <div class="field">
                <label class="label">Nome</label>
                <div class="control">
                    <input class="input" type="text" name="nome" id="nome" required>
                </div>
            </div>
            <div class="field">
                <label class="label">Cognome</label>
                <div class="control">
                    <input class="input" type="text" name="cognome" id="cognome" required>
                </div>
            </div>
            <div class="field">
                <label class="label">Tel</label>
                <div class="control">
                    <input class="input" type="tel" name="tel" id="tel" required>
                </div>
            </div>
            <div class="field">
                <label class="label">Email</label>
                <div class="control">
                    <input class="input" type="email" name="email" id="email" required>
                </div>
            </div>
            <div class="field">
                <label class="label">Password</label>
                <div class="control">
                    <input class="input" type="password" name="pwd" id="pwd" required>
                </div>
            </div>
            <div class="field">
                <button @click="onRegistration" class="button is-primary">Registrati</button>
            </div>
        </form>
    </div>
</template>