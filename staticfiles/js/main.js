// ...existing code...

document.getElementById('searchInput').addEventListener('input', function () {
    const query = this.value.toLowerCase();
    const gameCards = document.querySelectorAll('.card-list');

    gameCards.forEach(card => {
        const gameTitle = card.getAttribute('data-game').toLowerCase();
        if (gameTitle.includes(query)) {
            card.style.display = 'flex'; // Show matching cards
        } else {
            card.style.display = 'none'; // Hide non-matching cards
        }
    });
});

// ...existing code...