


// load a map
// var mymap = L.map('map').setView([51.505, -0.09], 13); 

// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     attribution: '© OpenStreetMap contributors'
// }).addTo(mymap);




// evenement pour recup la ville demandé et la date quand on lcique sur le boutton 
var bouton = document.getElementById("monBoutton");

bouton.addEventListener("click", async function() {

    event.preventDefault();
    var city= document.getElementById("location-input").value;
    var date =  document.getElementById("date").value;
    var unixTimestamp = convertDateToTimestamp(date);

    document.getElementById('test_insert').innerHTML = "";

    insertText("test_insert",city);
    insertText("test_insert",date);    
    insertText("test_insert",unixTimestamp);


    //  ok jusque la
    

    // protocoles asynchrone

    // appel de l'api pour requeter la base de données

    var cible ="http://127.0.0.1:8001/pull/";
    var requete = encodeURIComponent(city)+"/"+date.replace(/\//g, "_");
    // var requete = "predictions";
    console.log(cible+requete);

    var response = await call(cible , requete);
    //console.log(response);
    insertText("test_insert",response);


    
    //  si rien trouvé  => log pas d'info sur cette ville 

    //  sinon suite 

    // appel de api nlp endpoint ttt
    // cible = 
    // requete = 
    // var data = await call(cible , requete)

    // injection result ttt dans document
    // insertText (ttt, data )

    // appel de api nlp endpoint tts
    // cible = 
    // requete = 
    // var data = await call(cible , requete)


    // injection result tts dans document
});


// fonction pour injecter des données dans un document 
//  function insertAudio(destination, data){

//      const newEl = document.createElement("p",{'class':"inserted"});
//      newEl.innerText=data;

//      const cible = document.getElementById(destination);
//      cible.appendchild(newEl);

//      const audioElement = document.createElement('audio');
//      audioElement.controls = true; // Ajouter les contrôles de lecture
//      audioElement.src = audioURL;

// }


// fonction pour injecter des données dans un document 
function insertText (destination, data){

    const newEl = document.createElement("p",{'class':"inserted"});
    newEl.innerText=data;

    const cible = document.getElementById(destination);
    cible.appendChild(newEl);

}


// Fonction pour appel api 
async function call (cible,requete) {

    console.log(`tentative de connection a ${cible}`);

    db_answer = await fetch(cible+requete, { 
                    method: "GET"
                    })//.then(response => {return response.json()}); 

    return db_answer.text(); 

}
  

// Fonction pour ajouter une option à la liste déroulante
function addOption(selectElement, text, value) {
    var option = document.createElement("option");
    option.text = text;
    option.value = value;
    selectElement.add(option);
}


// Fonction pour obtenir la date de demain
function getNextDate(date, daysToAdd) {
    var newDate = new Date(date);
    newDate.setDate(newDate.getDate() + daysToAdd);
    return newDate;
}


// Fonction de conversion
function convertDateToTimestamp(dateString) {
    // Diviser la chaîne de caractères en jour, mois et année
    const [day, month, year] = dateString.split('/');

    // Créer un objet Date
    // Attention : mois - 1 car les mois commencent à 0 dans JavaScript
    const dateObject = new Date(`${year}-${month}-${day}`);

    // Obtenir le timestamp UNIX
    const timestamp = dateObject.getTime();

    return timestamp;
}
