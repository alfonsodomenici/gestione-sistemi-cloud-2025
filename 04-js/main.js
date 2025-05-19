import { prodotto } from "./funzioni.js";

//prendo i 4 elementi che mi servono dal DOM

const n1 = document.querySelector("#n1");

const n2 = document.querySelector("#n2");

const btn = document.querySelector("button[type='submit']");

const btnReset = document.querySelector("button[type='button']");

const result = document.querySelector("#result");

const form = document.querySelector("form");

const onBtnClick = (e) => {
    e.preventDefault(); //evita il refresh della pagina
    if(form.checkValidity() === false) {
        form.reportValidity();
        return;
    }   
    const risultato = prodotto(parseInt(n1.value),
        parseInt(n2.value));
    result.textContent = risultato;
}

const onBtnResetClick = (e) => {
    form.reset();
    result.textContent = "";
}

btnReset.addEventListener("click", onBtnResetClick);
btn.addEventListener("click", onBtnClick);