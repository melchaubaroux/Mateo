// JavaScript
var mymap = L.map('map').setView([51.505, -0.09], 13); // Définissez les coordonnées du centre de la carte et le niveau de zoom initial

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(mymap);
