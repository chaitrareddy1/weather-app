async function fetchWeather(city) {
    const response = await fetch(`/weather?city=${city}`);
    const data = await response.json();
    document.getElementById("currentWeather").textContent = JSON.stringify(data);
    updateChart(data);
}

function updateChart(data) {
    // Chart.js logic to update weather data on the graph
}

fetchWeather("Delhi");
