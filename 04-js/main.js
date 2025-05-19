import { prodotto } from "./funzioni.js";

//prendo i 4 elementi che mi servono dal DOM

const n1 = document.querySelector("#n1");

const n2 = document.querySelector("#n2");

const btn = document.querySelector("button");

const result = document.querySelector("#result");


const onBtnClick = () => {
    console.log("click");
    const risultato = prodotto(parseInt(n1.value),
        parseInt(n2.value));
    result.textContent = risultato;
}

btn.addEventListener("click", onBtnClick);