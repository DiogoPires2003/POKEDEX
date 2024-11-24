document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('input');
    const pokemonCards = document.querySelectorAll('.carta');

    searchInput.addEventListener('input', function () {
        const searchValue = searchInput.value.toLowerCase();

        pokemonCards.forEach(function (card) {
            const pokemonName = card.querySelector('.carta-nom').textContent.toLowerCase();

            // Compara el nombre del Pokémon con el valor del input (parcial o completo)
            if (pokemonName.includes(searchValue)) {
                card.style.display = 'block';  // Muestra la carta si coincide
            } else {
                card.style.display = 'none';   // Oculta la carta si no coincide
            }
        });
    });
});
