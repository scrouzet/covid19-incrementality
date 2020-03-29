# An incrementality study of the impact of COVID-19 in France

Aim: quantify death increase due to COVID-19 in France at the department level.

## References

- https://medium.com/@davidbessis/coronavirus-the-core-metrics-we-should-be-looking-at-2ca09a3dc4b1

## Data sources

- Death data form INSEE (French Statistic Agency) : https://www.data.gouv.fr/fr/datasets/fichier-des-personnes-decedees/
- Geography referential (commune and departement) : https://geo.api.gouv.fr
- Population data time serie from INSEE : https://www.insee.fr/fr/statistiques/1893198
- Population data time serie from INSEE - 2020-03-27 Weekly update for Covid : https://www.insee.fr/fr/information/4470857
- Number of admissions in hospitals due to influanza 2010-2020 from Sante Publique France : (https://www.santepubliquefrance.fr/)

# Methodology

## Data preparation : 
- Collection and concatenation of yearly death data (1990=> 2019)
- Deleted " replaced with white space
- retreated  dates : removed lines with invalid birth or death dates (0,72% of cases)
- fitler death dates> 1970
- join with geography referential to assiciate commune with department
- correction of department for specific geographies (Lyon, Paris, Marseille with arrondissement code instead of comune code in INSEE File)
- Grouping by death department, death date, sex, age, year of observation
- Year 1997 and 2003 should be removed from any analysis (1997 data seem invalid and 2003 is an outlier due to specific heat wave in France in August)

## Colonnes du fichier  : data/INSEE_deces_2010_2019.zip
- year of observation (annee_comptabilisation) = year of the yearly file where the death has been accounted for. (2019 = deces_2019.txt). Please note that a yearly file contains death dates from previous yeras due to delay in data collection at insee. All files must be concatenated to get a complete view of death for a given year. Duplicate records are already removed.
- sexe : 1 = Male / 2 = Female
- age : age at death time
- departement_deces : department code of the commune where death happend. Note that some department are not valid in the repository : 1% death in "99" departement, non significative death cases in "98" department. The department name and associated region is provided in the geography referential
- date_deces : death_date
- nb_deces : count of deceased person, grouped by (anneee_comptabilisation, sex, age, departement_code,  date_deces)

## Modélisation
WORK IN PROGRESS
- Model by age group at the level of French *départements*
- redressement des données hebdo de l'INSEE pour estimer l'effet de décallage dans la remontée des information (délai entre survenance du délai et comptabilisation par l'INSEE)

## How to

To generate a pickle file ready for analysis based on the years 2010 to 2019:

```bash
python preprocess.py -f INSEE_deces_2010_2019
```

This will create a pickle file in a `preprocessed_data` folder containing a pandas dataframe, aggregated by "departement" id number. `weeknumber_year.ipynb` is a simple example notebook to see what the data look like.


## Installation

You need to install git-lfs to retrieve the large data:
1. follow the [Installing Git Large File Storage](https://help.github.com/en/github/managing-large-files/installing-git-large-file-storage) guideline
2. read the [Configuring Git Large File Storage](https://help.github.com/en/github/managing-large-files/configuring-git-large-file-storage)

The following steps must be performed on a Anaconda prompt console, or 
alternatively, in a Windows command console that has executed the 
`C:\Anaconda3\Scripts\activate.bat` command that initializes the `PATH` so that
the `conda` command is found.

1. Clone the repository:
    ```
    $ git clone git@github.com:scrouzet/covid19-incrementality.git
    $ cd covid19-incrementality
    ```
    
2. Create a virtual environment with all dependencies.
    ```
    $ conda env create -f environment.yaml
    ```
    
3. Activate the environment and install this package (optionally with the `-e` flag).
    ```
    $ conda activate covid19inc-env
    $ pip install -e .
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
