# covid19-incrementalite
Etude d'incrementalité des effets du COVID-19.
Objectif : identifier la surmortalité dûe au COVID-19 à la maille département.

## Références

- https://medium.com/@davidbessis/coronavirus-the-core-metrics-we-should-be-looking-at-2ca09a3dc4b1

## Sources

Fichiers des décès de l'INSEE : https://www.data.gouv.fr/fr/datasets/fichier-des-personnes-decedees/

Fichiers des communes et association commune => Departement : geo.api.gouv.fr

Fichier de la population au 1er janvier par département : https://www.insee.fr/fr/statistiques/1893198

# Méthodologie

## Préparation des données : 
- Collecte et concaténaton des fichiers annuels (2000=> 2019)
- Suppression des " remplacées par des espaces
- Retraitement des dates : élimination des dates invalides : ~
- filtre sur les dates de décès > 1970
- jointure sur les codes insee de la commune de décès => Département
- retraitement pour corriger le cas des arrondissements Lyon, Paris, Marseille (pas un code insee commune)
- agrégation par Département de décès, date de décès, sexe, age, année de comptabilisation

## Colonnes du fichier  : data/INSEE_deces_2010_2019.zip
- annee_comptabilisation = année du fichier qui contient ces décès (2019 = deces_2019.txt) a noter un décalage entre date de décès et année de comptabilisation en raison du délai de remontée de l'information à l'INSEE
- sexe : 1 = Homme / 2 = Femme
- age : arrondi inférieur entre date de décès - date de naissance
- departement_deces : département rattache à la commune de décès. Attention, qq décès sont comptabilisés sur des départements "hors référentiel départements" : 1% des décès sur le département 99, négligeable sur 98.
- date_deces : date du décès
- nb_deces : somme du nombre de personnes décédées, regroupés par (anneee_comptabilisation, sex, age, département,  date_deces)

## Modélisation
- Modélisation par classe d'age et par département
- Retraitement de la canicule 2003
- redressement des données hebdo de l'INSEE pour estimer l'effet de décallage dans la remontée des information (délai entre survenance du délai et comptabilisation par l'INSEE)

## Installation

You need to install git-lfs to retrieve the large data:
    1. follow the [Installing Git Large File Storage](https://help.github.com/en/github/managing-large-files/installing-git-large-file-storage) guideline
    2. read the [Configuring Git Large File Storage](https://help.github.com/en/github/managing-large-files/configuring-git-large-file-storage)

Clone the repository:
```
    git clone git@github.com:scrouzet/covid19-incrementalite.git
```

## How to contribute

1. Fork this repo
2. Commit your code in your forked repo
3. Do a pull-request on the main repo and ask for code reviewers
4. Take into account the comments

For contributors
1. Make a branch "feat-short_name_feature"
2. Commit your code in this branch
3. Do a pull-request on the main repo and ask for code reviewers
4. Take into account the comments