# Particulate Matter Pollution and Air Pollution-Attributable Mortality in the United Kingdom

## Contributors

- Surya Chhabra
- Jonah Witte

## Summary

In this study, we examine how particulate matter pollution and air pollution-attributable deaths have changed in the UK over time through analysis of PM2.5 concentrations, PM2.5 emissions, PM10 emissions, and mortality values.

The core research question is: do PM2.5 concentrations, PM2.5 emissions, PM10 emissions, and air pollution-attributable mortality all have similar trends from the years when data from these datasets overlap? To address this question, we used publicly available data from the World Health Organization and UK government sources (i.e., the UK Department for the Environment, Food and Rural Affairs). The PM2.5 concentration data reflects air quality measured over time, and the emissions data indicates how many tonnes of PM2.5 and PM10 were discharged by sources in the UK per year. The WHO mortality data estimates annual deaths attributable to ambient air pollution. All three datasets contain annual values, so we cleaned and organized them to enable comparison between years.

The analysis of this study leverages three research questions: First, have PM2.5 concentrations increased or decreased over time? Second, do PM2.5 concentrations, PM2.5 emissions, PM10 emissions, and overall mortality due to air pollution all show the same trends over the same period? Third, to what extent do the diseases associated with deaths attributed to ambient air pollution correspond to PM2.5 concentrations? Finally, we discuss the limitations of using annual UK-level data for this kind of comparison.

The data above indicate a decline in PM2.5 concentration over the years observed. The years with overlap in each of the datasets demonstrate that both mortality values and PM2.5 and PM10 emissions have also declined. Furthermore, the scatter plot as well as the correlation table show that years with higher particulate matter have tended to experience higher mortality values than those without. PM2.5 emissions exhibited the greatest relationship to mortality among the variables examined.

In addition to the general findings noted above, there were additional details revealed when the disease-specific results were examined. Specifically, mortality values attributable to air pollution were not uniformly distributed among the various disease categories. For example, the disease category experiencing the most air pollution-attributable mortality was ischaemic heart disease, however, diseases such as stroke, chronic obstructive pulmonary disease, lung cancers, and acute lower respiratory infections were associated with differing patterns of mortality due to air pollution.

Results of this study should be interpreted with caution. The data are at the UK level and are aggregated by year so they do not provide information about exposure to an individual nor do they account for differences across locations or cause/effect relationships between air pollution and mortality. Additionally, other exposures that could affect mortality such as access to healthcare, population change, weather, and changes in relevant public policy were not included in this analysis. However, the project demonstrates the ability to clean, merge and analyse several public datasets to compare air pollution and mortality trends in a reproducible manner .

## Data Profile

This project uses public datasets about air pollution and mortality in the United Kingdom. All of the datasets used in the project are stored in the data_final folder in the repository.

At first, we planned to use London-level air quality data. Later, we changed the plan and used UK-level datasets instead. This made the datasets easier to combine because the PM2.5 concentration data, particulate matter emissions data, and WHO mortality data were all reported by year. Because of this, we used `year` as the shared column to connect the datasets.

### PM2.5 Concentration Dataset

**Repository location:** data_final/pm25_uk.csv

The PM2.5 concentration dataset contains yearly PM2.5 concentration values for the United Kingdom. It comes from the UK government ENV02 air quality statistics, specifically the PM2.5 tables. The original data is based on measurements from the Automatic Urban and Rural Network (AURN), which monitors major air pollutants at different sites. For this project, we use the cleaned UK-level CSV version instead of the raw spreadsheet-style file.

The cleaned file has one row for each year. The main columns are `year`, `geography`, and `pm25_concentration`. The `year` column shows the year of the observation, `geography` shows the location as the United Kingdom, and `pm25_concentration` gives the yearly PM2.5 concentration value.

This dataset is used to answer the first research question about how PM2.5 concentration changed over time. It is also used in the main comparison with air pollution-attributable mortality. This is useful because PM2.5 concentration measures what is present in the air, while emissions data measures how much particulate matter was released.

Data derived from the dataset does not include confidential/personal identifiable information which would raise privacy concerns (individual level data). The data comes from a publicly available, National Government Environmental Monitoring program. The data’s legal use requires appropriate citation and adherence to the Data Terms of Reuse from the National Government. The primary ethical issue is interpretation. As this data is at the national UK level, claims made about the local areas using this would be innaccurate. 

### WHO Air Pollution-Attributable Mortality Dataset

**Repository location:** data_final/who_uk.csv

The WHO mortality dataset comes from the World Health Organization Global Health Observatory. It contains estimates of deaths attributable to ambient air pollution. For this project, we use a cleaned UK-only version so it matches the UK-level pollution datasets.

The cleaned file, `who_uk.csv`, has one row for each year. The main columns are `year`, `geography`, and `mortality_value`. The `year` column shows the year, `geography` shows the location as the United Kingdom, and `mortality_value` gives the estimated number of air pollution-attributable deaths for that year.

This dataset is important because it provides the health outcome used in the project. We compare these mortality values with PM2.5 concentration, PM2.5 emissions, and PM10 emissions during the years where the datasets overlap.

A separate disease-specific version is also created for the additional disease breakdown question. 

**Repository location:** data_final/who_disease_uk.csv

The WHO has compiled a disease-specific dataset containing the same disease categories as the original WHO data. The dataset contains information on the year, disease category, and the mortality value for each disease category, including all-causes of mortality and disease-specific health outcomes such as: ischaemic heart disease, chronic obstructive pulmonary disease, stroke, lung cancer, and acute lower respiratory infections.

This dataset can be used to compare air pollution-attributable mortality rates across different disease categories. Additionally, it allows for comparisons of disease-specific mortality rates to PM2.5 concentrations.

As the WHO data is aggregate public health data, there is little privacy risk associated with its use because the data does not contain people’s names, addresses, or individual medical record. Nevertheless, it is still necessary to exercise caution in the interpretation of all health-related data in regard to the conclusions drawn from using it for the purposes of this project by making aggregate-level claims only and by not making claims that PM2.5 has directly caused the death of any individual; only that there is an association between the aggregate mortality estimates and the annual PM2.5 concentrations.

### PM2.5 Emissions Dataset

**Repository location:** data_final/emissions.csv

The PM2.5 emissions dataset is a cleaned version of the UK government particulate matter emissions data. The original source reports annual PM10 and PM2.5 emissions in the UK. For the main integrated dataset, we use the PM2.5 emissions values so they can be compared with PM2.5 concentration and air pollution-attributable mortality.

The cleaned file includes `year`, `geography`, and `emissions_thousand_tonnes`. The `emissions_thousand_tonnes` column gives the amount of PM2.5 emitted each year, measured in thousand tonnes. This dataset helps compare released particulate matter with measured PM2.5 concentration in the air and with mortality values during the overlapping years.

This dataset is publicly available from a UK government source and does not contain individual-level or private information. The main legal and ethical responsibilities are to cite the source, follow the reuse terms, and avoid overclaiming. Since the data is annual and UK-level, it cannot show individual exposure or local pollution differences.

### Final Integrated Dataset

**Repository location:** data_final/final_data.csv

The final integrated dataset is made up of the cleaned PM2.5 concentration dataset, the cleaned PM2.5 emissions dataset, and the cleaned WHO mortality dataset. It is set up as a table with columns for `year`, `geography`, `pm25_concentration`, `emissions_thousand_tonnes`, and `mortality_value`.

The integration uses `year` as the main shared attribute because all of the datasets show values for each year. The `geography field is set to the United Kingdom so that the datasets can be compared at the same level of geography. This combined file is the main dataset that is ready for analysis to compare PM2.5 levels, PM2.5 emissions, and death rates.

The final integrated dataset contains missing values where one source does not cover the same years as the others. This is expected because the emissions data covers a longer period than the PM2.5 concentration and mortality data. Rather than filling or estimating missing values, the analysis uses overlapping years when comparing mortality with pollution indicators. This keeps the analysis transparent and prevents invented values from affecting the results.

### Relationship Between the Datasets

This project contains multiple datasets to support the project’s research questions. The dataset on PM2.5 concentration looks to answer the PM2.5 concentration levels that have been measured over time. The datasets on emissions show how PM2.5 and PM10 have changed as well as how they may be compared to mortality data for said pollutants. The WHO mortality datasets provide health outcomes in the form of the total air pollution attributable mortality and the separate categories of disease for air pollution attributable mortality.

The datasets are complementary because they provide information relating to the various components of the relationship between air pollution and health. Concentration datasets are measurements of air pollution, emissions datasets are measurements of emissions released to the environment, and the mortality datasets provide estimates of the health effects that will occur as a result of the air pollution emitted into the environment. The datasets also share a ‘year’ field and can be combined to provide an overall description of the relationship between air pollution and health.

There are ethical and legal limitations for citation, responsible reuse, and careful interpretation associated with this research. While the data comes from publicly available government and international organization sources, there are no identifiable individuals that may have privacy concerns because of the nature of the aggregated data. Furthermore, the data is aggregated on an annual basis and is limited to a national-level of aggregation, which means that the project cannot make individual, regional or causal claims on the basis of the datasets. The main interpretations of this study will be based on the identification of associations and trends between the various datasets, as opposed to providing proof that a specific pollutant has caused to a change in the mortality rate.

## Data Quality

The datasets were cleaned and then evaluated for completeness, consistency, validity, duplicates, and whether they would integrate well into one another. Overall, cleaned data are available for use in descriptive trend analysis and visualizing processed data, except the primary quality limitation is that each of the cleanest source datasets has a different time frame.

After the cleaning process, all of the individual cleaned datasets are mostly complete. The cleaned PM2.5 Concentration data set (data_final/pm25_uk.csv) has one entry each year for the time range of 2009 through 2024. The cleaned WHO mortality data set (data_final/who_uk.csv) has one entry each year for the years 2010 through 2019. The cleaned emissions data set (data_final/emissions.csv) has one entry each year for the time range of 1970 through 2024, and the cleaned emissions year-wise data set (data_final/emissions_yearwise.csv) has one entry each year through 1970 through 2024 and includes columns individually for PM10 and PM2.5 emissions. There are no missing entries in the columns of interest for analysis.

The final data set that we will integrate (data_final/final_data.csv) has 55 rows (Records) and 5 columns (fields): `year`, `geography`, `pm25_concentration`, `emissions_thousand_tonnes`, and `mortality_value`. It includes years from 1970 to 2024 since the emissions dataset has the largest time range.

The missing data points were left as missing in the integrated dataset. This way the limitations of the data are clear. When comparing deaths, emissions, and concentrations, only the years where data exists are used to avoid creating unintentional data and keep the visualizations connected to the raw data.

The cleaned data also has consistent formats. Year values were converted from date values to integers, measurement values were converted from string values to numeric values, and geographic labels were standardized to "United Kingdom". Geographic labels and formats are inconsistent among the raw datasets, for example WHO raw data has periods and locations as column headings, but the cleaned project files have year and geography column headings. Also, since the cleaned project files have PM10 and PM2.5 emissions in separate columns, the emissions dataset was reshaped to compare both types of emissions.

Duplicate checks also occurred. Once filtered and reshaped, there were no duplicate rows in the cleaned project datasets. This is important because during the integration of the datasets by `year`, any duplicate `year` records would have caused incorrect one-to-many merging or multiple occurrences of the same value in the final dataset.

The primary integration key is `year`, which works for the project since all datasets provide values annually. However, using `year` as the shared key limits the types of conclusions that can be drawn. The analysis compares aggregate annual trends for the UK, not exposure on a daily basis, localized air pollution, or individual health outcomes; thus, the results can show patterns of association, but they cannot establish a cause/effect relationship between PM and differences in mortality.

In general, the data quality is sufficient to address the research questions of the project. The cleaned files are organized, quantitative, consistent, and appropriate for merging and visualizing the information. The major limitation is the lack of consistent temporal coverage across the source datasets, especially the shorter duration between the time periods that report mortality, which will be addressed through documentation of missing values and by limiting mortality comparisons to years in which the source datasets overlap.

## Data Cleaning

Before integrating three datasets into one dataset, there were some data preparation (or cleaning) steps necessary for the datasets to be integrated into a tidy form, as well as standardizing column names and data types, and making sure they were ready for joining by year and geographic area of the UK.

There was much more structural cleaning performed on the PM2.5 concentration data than for the two other datasets. The original PM2.5 dataset was in a government table format in a spreadsheet and contained rows with headings, notes, and columns named `Unnamed`, none of which are part of the data collected. All of those extra headings, notes and unnamed columns were removed from the cleaned PM2.5 dataset so it contains only data for years and annual PM2.5 concentrations. After the data was cleaned up, the three remaining fields were assigned new column names of `year`, `geography`, and `pm25_concentration`. Year values were updated to be integers and pm25_concentration values were updated to be numeric. Additionally, the cleaned PM2.5 data was filtered at this point to only retain annual summary "All sites (mean)" PM2.5 concentrations, for use at the national UK-level integration step.

The WHO dataset is more structured; however, it also contains multiple sex-specific and disease-specific records (one for males, one for females and multiple lists for disease). In our main integrated dataset, we filtered the WHO dataset to include only the records for the United Kingdom, both sexes, and all cause mortality values attributed to ambient air pollution. By this filtering method, we produced only one value of mortality for each year of the UK, so it was then suitable to use in combination with the annual dataset for both pollution and emis­sions. Because of the fact that we are only interested in three specific columns, the columns of the WHO dataset were renamed to simpler terms including `year`, `geography`, and `mortality_value`, and the mortality values were converted to numeric representations. In addition, a separate disease-specific WHO dataset was prepared so that we could assess mortality across individual diseases and health conditions.

The emissions dataset was also cleaned up for our purposes, including renaming the columns to standardize naming conventions and converting both the years and emissions values to numeric representations. In addition to the primary emissions file, an annual emissions file was also created and structured so that for each year there are separate columns for PM2.5 and PM10 emissions. By reorganizing the emissions data into yearly files that are in similar formats, it makes comparing the two emissions types directly much more simple.

After the individual datasets were cleaned and integrated using common criteria such as year and UK-level geography, the final integrated dataset combined PM2.5 concentration, PM2.5 emissions, and WHO mortality data. Because the datasets cover different year ranges, some values in the final integrated dataset remain missing values. These will remain as is, as they represent real differences in data collection between data sets rather than problems with data entry. As a result, all of the data sets have been cleaned and made to be compatible for use together while still maintaining their original source characteristics.

# Analysis and Visualizations

## Research Questions

### Research Question 1
How has PM2.5 concentration changed over time?

### Research Question 2
How do PM2.5 concentration, PM2.5 emissions, and PM10 emissions compare with air pollution-attributable mortality over time?

### Research Question 3
How does air pollution-attributable mortality differ across disease categories, and how do those disease-specific mortality values compare with PM2.5 concentration?

## Research Question 1: How has PM2.5 concentration changed over time?

This question uses the cleaned PM2.5 concentration dataset. It shows how measured PM2.5 concentration changed during the available years. 

See Figure (1):

![Figure 1: PM2.5 concentration over time](figures/(1)_pm25_concentration_over_time.png)

Start: 2009 12.3933081899161

End: 2024 7.15113554252513

Percent change: -42.3 %

### Interpretation

PM2.5 concentration generally decreased over the available years. There are some year-to-year changes, but the overall pattern shows lower PM2.5 concentration toward the end of the period than at the beginning. This suggests an improvement in measured PM2.5 air quality over time.

## Research Question 2: How do PM2.5 concentration, PM2.5 emissions, and PM10 emissions compare with air pollution-attributable mortality over time?

See Figure (2):

![Figure 2: mortality_over_time](figures/(2)_mortality_over_time.png)

See Figure (3):

![Figure 2: pm25_emissions_over_time](figures/(3)_pm25_emissions_over_time.png)

See Figure (4):

![Figure 2: pm25_emissions_vs_concentration](figures/(4)_pm25_emissions_vs_concentration.png)


Mortality change: -29.78 %

PM2.5 emissions change: -18.42 %

PM2.5 concentration change: -23.84 %

### Interpretation

During the overlapping years, mortality, PM2.5 emissions, and PM2.5 concentration generally decrease. The PM2.5 emissions and concentration scatter plot also suggests that higher PM2.5 emissions tend to appear with higher PM2.5 concentration. These plots support a descriptive relationship between pollution indicators and mortality, but they do not prove causation.

### Add PM10 emissions to the mortality comparison

See Figure (5):

![Figure 5: indexed_emissions_and_mortality](figures/(5)_indexed_emissions_and_mortality.png)


See Figure (6):

![Figure 6: emissions_vs_mortality](figures/(6)_emissions_vs_mortality.png)
### Interpretation

The correlation table shows a strong positive relationship between particulate matter emissions and air pollution-attributable mortality during the overlapping years. PM2.5 emissions have a stronger correlation with mortality, about 0.97, while PM10 emissions have a correlation of about 0.87. This suggests that PM2.5 emissions follow the mortality pattern more closely than PM10 emissions in this dataset.

The scatter plot supports this result. Years with higher PM2.5 and PM10 emissions generally also have higher mortality values. PM10 emissions are higher in total because PM10 includes a larger particle size range than PM2.5. However, PM2.5 emissions appear to align more closely with mortality during the same period.

The indexed line plot is useful because emissions and mortality are measured on different scales. By setting each series to 100 in the first overlapping year, the plot compares relative change over time instead of raw values. PM2.5 emissions, PM10 emissions, and mortality all generally decline, but mortality declines more sharply. By the final overlapping year, mortality falls to about 70% of its starting value, while PM2.5 emissions remain around 82% and PM10 emissions around 85%.

Overall, the results suggest that particulate matter emissions and mortality move in the same general direction, with PM2.5 emissions showing the strongest association with mortality. However, this does not prove causation. The data is annual and UK-level, so it cannot account for individual exposure, regional differences, demographic changes, healthcare access, weather, or other factors that may also affect mortality.

## Research Question 3: How does air pollution-attributable mortality differ across disease categories, and how do those disease-specific mortality values compare with PM2.5 concentration?

The cleaned `who_uk` dataset used earlier keeps only the all-cause mortality value. For this additional question, a new disease-specific WHO dataset is created from the raw WHO file so that disease categories can be compared.

### Disease-specific mortality trends over time

This plot compares air pollution-attributable mortality across disease categories. The “All causes” category is excluded because it is a total category and would dominate the disease-specific lines.

See Figure (7):
![Figure 7: disease_mortality_over_time](figures/(7)_disease_mortality_over_time.png)

### Average mortality by disease category

This bar chart summarizes which disease categories have the highest average air pollution-attributable mortality across the available years.

See Figure (8):
![Figure 8: average_disease_mortality](figures/(8)_average_disease_mortality.png)

### PM2.5 concentration compared with disease-specific mortality

### Interpretation

The disease breakdown shows that air pollution-attributable mortality is not the same for every disease category. Ischaemic heart disease has the highest average mortality by far. Stroke, acute lower respiratory infections, and chronic obstructive pulmonary disease are lower, and lung cancers are the lowest among the categories shown.

Over time, most disease categories generally decrease from 2010 to 2019. Ischaemic heart disease has the clearest downward trend, but it still remains much higher than the other categories. Stroke and lung cancers also decrease overall. Acute lower respiratory infections and chronic obstructive pulmonary disease change more unevenly, with some small increases and decreases across the years.

The correlation table compares PM2.5 concentration with mortality for each disease category. Lung cancers, ischaemic heart disease, and stroke have the strongest positive correlations with PM2.5 concentration. This means that, in the years where PM2.5 concentration was higher, mortality values for these diseases also tended to be higher.

This does not prove that PM2.5 directly caused these deaths. It only shows that some disease categories move more closely with PM2.5 concentration in this annual UK-level dataset.

## Findings

The analysis shows that particulate matter pollution and air pollution-attributable mortality generally declined in the United Kingdom during the years covered by the cleaned datasets. The PM2.5 concentration data show a clear downward trend from 2009 to 2024. PM2.5 concentration decreased from approximately 12.39 in 2009 to 7.15 in 2024, a decline of about 42.3%. Although there are year-to-year fluctuations, the overall pattern suggests improved PM2.5 air quality over time.

The strongest overlap across the PM2.5 concentration, emissions, and mortality datasets occurs from 2010 to 2019. During this period, all three key measures decreased. Air pollution-attributable mortality declined from 31,805 deaths in 2010 to 22,333 deaths in 2019, a decrease of about 29.8%. PM2.5 emissions declined from about 79.99 thousand tonnes to 65.26 thousand tonnes, a decrease of about 18.4%. PM2.5 concentration declined from about 12.97 to 9.88, a decrease of about 23.8%. These results suggest that reductions in particulate matter pollution occurred at the same time as reductions in estimated air pollution-attributable mortality.

The visualizations support this pattern. The PM2.5 concentration line chart shows a general decline over time, while the mortality and emissions line charts also show downward trends during the overlapping years. The scatter plot comparing PM2.5 emissions and PM2.5 concentration suggests that higher PM2.5 emissions are generally associated with higher PM2.5 concentration. This relationship is also reflected in the correlation value of about 0.95 between PM2.5 concentration and PM2.5 emissions.

The comparison between particulate matter emissions and mortality shows a strong positive relationship. PM2.5 emissions have a correlation of about 0.97 with mortality, while PM10 emissions have a correlation of about 0.87 with mortality. This indicates that PM2.5 emissions follow the mortality trend more closely than PM10 emissions in this dataset. The indexed line chart is especially useful because it puts emissions and mortality on the same relative scale. It shows that PM2.5 emissions, PM10 emissions, and mortality all generally decline after 2010, although the rate of decline differs across the measures.

The disease-specific analysis shows that air pollution-attributable mortality is not evenly distributed across disease categories. Ischaemic heart disease has the highest average mortality, with an average value of about 13,668. Acute lower respiratory infections average about 4,277, stroke about 3,953, chronic obstructive pulmonary disease about 2,934, and trachea, bronchus, and lung cancers about 1,819. Most disease categories decline overall from 2010 to 2019, although some categories show more uneven year-to-year movement.

The correlation between PM2.5 concentration and disease-specific mortality is strongest for trachea, bronchus, and lung cancers at about 0.91, followed by ischaemic heart disease at about 0.86 and stroke at about 0.83. Chronic obstructive pulmonary disease shows a moderate correlation of about 0.63, while acute lower respiratory infections show a weaker correlation of about 0.21.

Overall, the findings show consistent descriptive evidence that particulate matter pollution and air pollution-attributable mortality declined together in the UK. However, the analysis is based on aggregate yearly data, so these results should be interpreted as associations rather than proof that pollution reductions directly caused the observed mortality decreases.

## Future Work

The analysis could be improved by expanding the range of data used. This project focuses mainly on national-level UK data, which is useful for identifying broad trends. However, national averages are not good for impacting real people. Future work could examine regional or local air quality data within the United Kingdom, such as in London or other major cities. This would make it possible to compare areas with higher and lower pollution levels and to investigate whether changes in air pollution and mortality differ by region and make it easier to identify the causes and prevention methods.

Another possible improvement would be to add more health and demographic variables. Air pollution-attributable mortality may be influenced by factors such as age distribution, population size, smoking rates, health care access, income, and urbanization. Future work could incorporate population-adjusted rates rather than only raw mortality values. This would make the analysis more meaningful because the number of deaths can change partly because the population changes. Age-standardized rates would be especially useful because air pollution-related diseases are strongly affected by population aging.

The project could also include more complex models beyond correlation. Our current analysis is mostly descriptive and focuses on trends, correlations, and visual comparisons. These are useful for identifying patterns, but they do not establish causation. Future work could use regression models to test whether PM2.5 concentration or emissions predict mortality after accounting for year, population, or other variables. Time-series methods could also be useful because air pollution exposure and health outcomes may have delayed effects. For example, some diseases may respond to long-term pollution exposure rather than only pollution levels in the same year. If there was a study tracking the health of people living in the UK and their exposure to air pollution as well as any health conditions, this would be a very interesting thing to combine with our current analysis as we could track long term affects of air pollution. 

## Limitations / Challenges

One limitation is the datasets do not have the same year overlap for the measures examined; PM2.5 concentrations are not available over the same time period as the emissions data and mortality data. Thus, in the cleaned dataset the overlap is only for the years 2010 to 2019. Because of this, the analysis comparing mortality data will only include those years for which all of the necessary values are present.

Another limitation is the data has been aggregated to the annual UK level, therefore the comparison in the analysis is at the aggregate year level and not at an individual basis such as a person, neighbourhood or specific geographical area. Therefore, it is not possible to show whether individuals in one geographical area with higher PM10 exposure had lower or higher mortality values than those in other areas. The analysis also will not be able to account for the effects of other confounding variables such as changes in population size, age distribution, healthcare changes, the weather, smoking rate, or changes of policy.

The analysis also compares indicators to different events; PM2.5 concentrations measure the concentration of PM2.5 in the air, and PM2.5 and PM10 emissions measure the quantity of PM2.5 and PM10 emitted. Although PM2.5 concentrations and PM2.5 and PM10 emissions are related, they are not the same; therefore the results should be viewed as general trends and associations rather than a cause-and-effect relationship.

Overall, the dataset can be used successfully for descriptive trend analysis and comparison, but cannot be used to prove that a specific pollutant caused a change in mortality value.

## References

Department for Environment, Food & Rural Affairs. (2025). *ENV02: Air quality statistics*. GOV.UK. Retrieved from https://www.gov.uk/government/statistical-data-sets/env02-air-quality-statistics

Department for Environment, Food & Rural Affairs. (2026). *Emissions of air pollutants in the UK: Particulate matter (PM10 and PM2.5)*. GOV.UK. Retrieved from https://www.gov.uk/government/statistics/emissions-of-air-pollutants/emissions-of-air-pollutants-in-the-uk-particulate-matter-pm10-and-pm25

World Health Organization. (n.d.). *Air pollution attributable deaths, ambient*. Global Health Observatory. Retrieved from https://www.who.int/data/gho/data/indicators/indicator-details/GHO/ambient-air-pollution-attributable-deaths

Matplotlib Development Team. (n.d.). *Matplotlib: Visualization with Python*. Retrieved from https://matplotlib.org

Snakemake. (n.d.). *Installation*. Snakemake documentation. Retrieved from https://snakemake.readthedocs.io/en/stable/getting_started/installation.html#conda-install

The pandas development team. (2024). *pandas: Powerful Python data analysis toolkit*. Retrieved from https://pandas.pydata.org/
