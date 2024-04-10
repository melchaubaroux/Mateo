

# Postgres connection 
host="localhost"
database="suppliers"
user="postgres"
password="Plasma2020@"
options="-c search_path=public"


# eden global parameter 

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiODAwMTFhYmEtYzNlNy00YzY5LTliZGMtMGQ5OThkODk2OWU1IiwidHlwZSI6ImFwaV90b2tlbiJ9.N3jUN6ucg324ejC2D9BYZNTAi0awJ4BWdLsXqva1164"}

# eden ai connection llm


url_llm = "https://api.edenai.run/v2/text/chat"

prompt = """tu est presentateur meteo appelé mateo ,
            tu dois ecrire le texte pour ton journal meteo a partir des infos qui te sont fournit. """


# eden ai connection tts

url_tts = "https://api.edenai.run/v2/audio/text_to_speech"


test="Bonjour chers téléspectateurs, ici Mateo avec votre bulletin météo. Aujourd'hui, nous nous trouvons à Ville du Pont où la température est de 35.9 degrés Celsius avec une sensation de chaleur de 40.27 degrés en raison de l'humidité de 30%. Le vent souffle à une vitesse de 3 km/h en provenance de l'est (80°). Le ciel est voilé avec 90% de couverture nuageuse. Pas de précipitations prévues dans les prochaines heures. La pression atmosphérique est de 1005 hPa. Restez au frais et hydr"

payload_tts = {
    "providers": "google,amazon", "language": "en-US",
    "option": "MALE",
    "text": test,
    "fallback_providers": ""
}


