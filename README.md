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

## List of files : 
- Deces_yyyy-yyyy.zip = civil status register of death, for years yyyy (death accounted for in thoses years)
- commune.csv = list of administrative area level 3 in France
- departments.csv = list of administrative area level 2 in France
- INSEE - year x dept x sex x age - population.csv = historical series of population in each department, by age class and sex 

## Data Model : Fields and names
Civil status files : 
- lastname	Last name of dead person
- firstname	First name of dead person
- sex	Sex of dead person (M = Male / F = Female)
- birth_date_txt	Birth Date in text format (format YYYYMMDD). MM or DD = 00 when unknown
- birth_commune_code	Commune code of birth place (may not exist in referrential for historical communes)
- birth_commune_name	Commune name of birth place
- birth_country_name	Country of birth
- death_date_txt	Birth Date in text format (format YYYYMMDD). MM or DD = 00 when unknown
- death_commune_code	Commune code of death(may not exist in referrential for historical communes)
- death_register_number	Number of death in civil status register (not always a number)
- birth_date	Valid birth date (YYYY-MM-DD) format. Empty if invalid or unknown
- death_date	Valid death date (YYYY-MM-DD) format. Empty if invalid or unknown

Geographical referential files  :
- commune_code	Code of commune (3rd level administrative subdivision of France)
- commune	Name of commune (3rd level administrative subdivision of France)
- population	Headcount of population as of 01/01/2020 (estimated)
- departement_code	Code of department (2nd level administrative subdivision of France)
- departement	Name of department (2nd level administrative subdivision of France)
- region_code	Code of région (1st level administrative subdivision of France)
- region	Name of region (1st level administrative subdivision of France)
- classe_age_5  age interval (5 years)

# Methodology

## Data preparation : (Files in/ preprocessed data/)
File : INSEE_deces_1990_2019_byweek.csv.gz
- Collection and concatenation of yearly death data (1990=> 2019)
- Deleted " replaced with white space
- retreated  dates : removed lines with invalid birth or death dates (0,72% of cases)
- fitler death dates> 1970
- join with geography referential to assiciate commune with department
- correction of department for specific geographies (Lyon, Paris, Marseille with arrondissement code instead of comune code in INSEE File)
- Grouping by death department, death date, sex, age, year of observation
- Year 1997 and 2003 should be removed from any analysis (1997 data seem invalid and 2003 is an outlier due to specific heat wave in France in August)


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
