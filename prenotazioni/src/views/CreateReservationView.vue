<script setup>

const onSave = () => {
    // Implement save logic here, e.g., send data to the server
    console.log('Reservation saved');
    // Redirect or show a success message
}
</script>

<template>
    <div class="columns is-centered mt-5">
        <form class="box column is-half">
            <p class="title has-text-centered">Prenotazione esami</p>

            <div class="field">
                <label class="label">Tipo esame</label>
                <div class="control">
                    <div class="select">
                        <select>
                            <option>Select dropdown</option>
                            <option>With options</option>
                        </select>
                    </div>
                </div>
            </div>
            <div class="field">
                <label class="label">Data</label>
                <div class="control">
                    <input class="input" type="date" name="date" id="date" required>
                </div>
            </div>
            <div class="field">
                <button @click.prevent="onSave" class="button is-primary">Salva</button>
            </div>
        </form>
    </div>
</template>