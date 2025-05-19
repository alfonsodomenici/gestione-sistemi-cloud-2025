const prodotto = (numero1, numero2) => {
    let conta = 1;
    let risultato = 0;
    while (conta <= Math.abs(numero2)) {
        risultato += numero1;
        conta++;
    }
    return numero2 < 0 ? -risultato : risultato;
}

export { prodotto };