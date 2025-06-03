<script setup>

const onLogin = (e) => {
    console.log('effettuare login');
}
</script>

<template>
    <div class="columns is-centered mt-5">
        <form class="box column is-half" @submit.prevent>
            <p class="title has-text-centered">Login</p>
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
                <button @click="onLogin" class="button is-primary">Login</button>
            </div>
        </form>
    </div>
</template>