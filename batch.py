import json

from meteo_france.fonctions import *
from db.fonctions import *


# check si le fichier json est trouvable  ou requete data gouv a la place 
try : 
   
    path="../data/cities.json"

    with open(path, 'r') as fichier:
        cities = json.load(fichier)

except:
    print("file not found at ./data so we fetch data.gouv")
    cities = get_france_city()[:1]


# requetes les previsions pour toutes les villes de françaises
data=list(get_france_fc(cities))



# integration de ces données dans la db :  

# recupere les noms et type de colonnes pour la db
col_type,col_name=get_colonne (data[0][1][0])
col_type=['varchar']+col_type
col_name=["city_name"]+col_name

table_name="predictions"


create_table (table_name,col_name,col_type)

insert_many(table_name,col_name,data)




















