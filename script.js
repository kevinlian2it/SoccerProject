document.getElementById('getRecommendations').addEventListener('click', async () => {
    const team = document.getElementById('teamSelect').value;
    const position = document.getElementById('positionSelect').value;

    try {
        const response = await fetch(`https://soccerproject.onrender.com/api/recommend?team=${team}&position=${position}`);
        const data = await response.json();

        const table = document.getElementById('recommendationTable');
        const tbody = table.querySelector('tbody');
        tbody.innerHTML = '';  // Clear previous rows

        if (data.error) {
            // Display error message
            table.style.display = 'none';
            alert(data.error);
        } else {
            // Populate table with recommendations
            data.forEach(player => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${player.Player}</td>
                    <td>${player.Age}</td>
                    <td>${player.Nation}</td>
                    <td>${player.League}</td>
                    <td>${player.Squad}</td>
                    <td>${player.Position}</td>
                    <td>${player.Predicted_Suitability.toFixed(2)}</td>
                `;
                tbody.appendChild(row);
            });

            table.style.display = 'table';
        }
    } catch (error) {
        console.error('Error fetching recommendations:', error);
        alert("There was an error fetching recommendations. Please try again later.");
    }
});
