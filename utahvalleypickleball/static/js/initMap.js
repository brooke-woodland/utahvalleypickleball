// Initialize and add the map
function initMap() {

    // Grab data and parse it
    const data = JSON.parse("{{data|escapejs}}");

    // The location of Provo
    const provo = { lat: 40.23469107929458, lng: -111.65817642354494 };

    // The map, centered at Provo
    const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 10.5,
    center: provo,
    });

    // loops through each coordinate object in data and adds it as a marker
    data.map(cd => {
        new google.maps.Marker({
            position: cd,
            map: map
        })
    });
}

window.initMap = initMap;