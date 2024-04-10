CREATE TABLE prevision (

    NUM_POSTE     INT, --numéro Météo-France du poste sur 8 chiffres
    NOM_USUEL     VARCHAR(255),--nom usuel du poste
    LAT           REAL,  --latitude, négative au sud (en degrés et millionièmes de degré)
    LON           REAL, --longitude, négative à l’ouest de GREENWICH (en degrés et millionièmes de degré)
    ALTI         INT , --altitude du pied de l'abri ou du pluviomètre si pas d'abri (en m)
    AAAAMMJJHHMN  DATE, --de la mesure (année mois jour heure minute)
    RR            REAL, --quantité de précipitation tombée en 6 minutes (en mm et 1/10)
    QRR            INT --code qualité de RR
);

-- Les valeurs du code qualité sont les suivantes :
--  9 : donnée filtrée (la donnée a passé les filtres/contrôles de premiers niveaux)
--  0 : donnée protégée (la donnée a été validée définitivement par le climatologue)
--  1 : donnée validée (la donnée a été validée par contrôle automatique ou par le climatologue)
--  2 : donnée douteuse en cours de vérification (la donnée a été mise en doute par contrôle automatique)
 

--LOAD DATA INFILE '/chemin/vers/votre/donnees.csv'
--INTO TABLE prevision
--FIELDS TERMINATED BY ',' ENCLOSED BY '"'
--LINES TERMINATED BY '\n'
--IGNORE 1 ROWS; -- Ignorer la première ligne si elle contient des en-têtes de colonnes



