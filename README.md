# covid19-incrementalite
Etude d'incrementalité des effets du COVID-19.
Objectif : identifier la surmortalité dûe au COVID-19 à la maille département.

## Références

- https://medium.com/@davidbessis/coronavirus-the-core-metrics-we-should-be-looking-at-2ca09a3dc4b1

## Sources

Fichiers des décès de l'INSEE :

Fichiers des communes et association commune => Departement: geo.api.gouv.fr

## Méthodologie

# Préparation des données : 
- Collecte et concaténaton des fichiers annuels (2000=> 2019)
- Suppression des " remplacées par des espaces
- Retraitement des dates : élimination des dates invalides : ~
- filtre sur les dates de décès > 1970
- jointure sur les codes insee de la commune de décès => Département
- retraitement pour corriger le cas des arrondissements Lyon, Paris, Marseille (pas un code insee commune)
- agrégation par Département de décès, date de décès, sexe, age, année de comptabilisation



# Modélisation
- Attention à agréger par année de comptabilisation avant de modéliser. J'ai laissé cette variable pour tenir compte de l'effet de retard dans la prise en compte des décès. L'année de comptabilisation correspond à l'année du fichier annuel des décès. 
