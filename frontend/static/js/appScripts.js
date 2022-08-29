// When page loads assign element with value1, make a request to the server, and update the element with value2 when resutl comes back
document.addEventListener('DOMContentLoaded', async (event) => {
    document.getElementById('conn_status').innerHTML = '<div>Loading...</div>';
    var response = await fetch('proxy/db_conn_status');
    const myJson = await response.json();
    // console.log(myJson);
    var isConnectedToDB = myJson.value;
    document.getElementById('conn_status').innerHTML = "<div>" + isConnectedToDB +"</div>";

    // Once connection to the DB is made, load form enabling adding values to DB
    if (isConnectedToDB) {
        // Loading a template form to show on page
        fetch('/static/templates/addItemTemp.html')
            .then(response => response.text())
            .then(text => document.getElementById('add_item_to_db').innerHTML = text);
    }

    // Once connection to the DB is made, print content of the DB
    if (isConnectedToDB) {
        // Read values from DB
        var response2 = await fetch('proxy/read_db');
        const myJson2 = await response2.json();
        // console.log(myJson2);
        var dbValues = myJson2.value;
        var elementBuilder = ""
        dbValues.forEach(function (item, index) {
            elementBuilder += "<div>" + item + "</div>";
        });
        document.getElementById('db_data').innerHTML = elementBuilder;
    }
});
