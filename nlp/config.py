
header = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiODAwMTFhYmEtYzNlNy00YzY5LTliZGMtMGQ5OThkODk2OWU1IiwidHlwZSI6ImFwaV90b2tlbiJ9.N3jUN6ucg324ejC2D9BYZNTAi0awJ4BWdLsXqva1164"}

url_text_to_text = "https://api.edenai.run/v2/text/generation"

prompt = """écrire le texte du journal météo
a la date fournis grâce aux informations qui te sont fournis
(exprime la date un autre format)  : """

payload_text_to_text = {
    "providers": "openai",
    "text": prompt,
    "temperature": 0.0,
    "max_tokens": 250,
    "fallback_providers": ""

}


url_text_to_speech = "https://api.edenai.run/v2/audio/text_to_speech"

payload_text_to_speech = {
    "providers": "openai", "language": "fr",
    "option": "MALE",
    "text": "",
    "fallback_providers": ""
}


