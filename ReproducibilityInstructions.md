# Reproducibility Instructions

This document describes the steps required to reproduce the data acquisition, cleaning, and visualization workflow for this project.

## 1. Download the PM2.5 concentration data

Go to the UK Government air quality statistics page:

https://www.gov.uk/government/statistical-data-sets/env02-air-quality-statistics

Download the following spreadsheet:

https://assets.publishing.service.gov.uk/media/685bba977d72089d1997609b/PM25_Tables_2024.ods

Open the `.ods` file and go to the Table2_1b sheet/page. Export that sheet as a CSV file and save it in the project directory.

Recommended save location:

```text
data_final/Table2_1b.csv
```

## 2. Download the UK particulate matter emissions data

Go to the UK Government particulate matter emissions page:

https://www.gov.uk/government/statistics/emissions-of-air-pollutants/emissions-of-air-pollutants-in-the-uk-particulate-matter-pm10-and-pm25

Download the following CSV files:

```text
https://assets.publishing.service.gov.uk/media/6983269a13622473b51ca9b2/fig03_particulate_matter_annual_emissions.csv
https://assets.publishing.service.gov.uk/media/698326c15a7e802e96d343c4/fig04_pm10_key_emission_sources.csv
```

Save these files in the project directory.

Recommended save locations:

```text
data_final/fig03_particulate_matter_annual_emissions.csv
data_final/fig04_pm10_key_emission_sources.csv
```

## 3. Download the WHO mortality data

Go to the World Health Organization Global Health Observatory indicator page:

https://www.who.int/data/gho/data/indicators/indicator-details/GHO/ambient-air-pollution-attributable-deaths

Download the data as a CSV file and save it in the project directory.

Recommended save location:

```text
data_final/b7450f71-eae9-4c95-98e4-022ddec4a93f.csv
```

## 4. Install and Run Snakemake

We used snakemake to automate our workflow. For the same results, this snakemake version was the one used to install and run our workflow.

```bash
conda install -c bioconda -c conda-forge snakemake-minimal
```

Source: https://snakemake.readthedocs.io/en/stable/getting_started/installation.html


From the project root directory, run:

```bash
snakemake -j1
```

This will execute the data cleaning workflow and generate the cleaned datasets.

Expected cleaned outputs:

```text
final_snake_data/pm25_uk.csv
final_snake_data/who_uk.csv
final_snake_data/emissions.csv
final_snake_data/final_data.csv
```

## 6. Run the visualization script

After the cleaned data files have been created, run the visualization script:

```bash
python scripts/run_visualizations.py
```

This will generate the project figures and save them in the `figures/` directory.

Expected visualization outputs:

```text
figures/(1)_pm25_concentration_over_time.png
figures/(2)_mortality_over_time.png
figures/(3)_pm25_emissions_over_time.png
figures/(4)_pm25_emissions_vs_concentration.png
figures/(7)_disease_mortality_over_time.png
figures/(8)_average_disease_mortality.png
```
