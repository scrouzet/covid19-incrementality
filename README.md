# covid19-incrementalite
Etude d'incrementalité des effets du COVID-19.
Objectif : identifier la surmortalité dûe au COVID-19 à la maille département.

## Références

- https://medium.com/@davidbessis/coronavirus-the-core-metrics-we-should-be-looking-at-2ca09a3dc4b1

## Sources

Fichiers des décès de l'INSEE : https://www.data.gouv.fr/fr/datasets/fichier-des-personnes-decedees/

Fichiers des communes et association commune => Departement : geo.api.gouv.fr

## Méthodologie

# Préparation des données : 
- Collecte et concaténaton des fichiers annuels (2000=> 2019)
- Suppression des " remplacées par des espaces
- Retraitement des dates : élimination des dates invalides : ~
- filtre sur les dates de décès > 1970
- jointure sur les codes insee de la commune de décès => Département
- retraitement pour corriger le cas des arrondissements Lyon, Paris, Marseille (pas un code insee commune)
- agrégation par Département de décès, date de décès, sexe, age, année de comptabilisation

# Colonnes du fichier  : data/INSEE_deces_2010_2019.zip
- annee_comptabilisation = année du fichier qui contient ces décès (2019 = deces_2019.txt) a noter un décalage entre date de décès et année de comptabilisation en raison du délai de remontée de l'information à l'INSEE
- sexe : 1 = Homme / 2 = Femme
- age : arrondi inférieur entre date de décès - date de naissance
- departement_deces : département rattache à la commune de décès. Attention, qq décès sont comptabilisés sur des départements "hors référentiel départements" : 1% des décès sur le département 99, négligeable sur 98.
- date_deces : date du décès
- nb_deces : somme du nombre de personnes décédées, regroupés par (anneee_comptabilisation, sex, age, département,  date_deces)

# Modélisation
- Attention à agréger par année de comptabilisation avant de modéliser. J'ai laissé cette variable pour tenir compte de l'effet de retard dans la prise en compte des décès. L'année de comptabilisation correspond à l'année du fichier annuel des décès. 
