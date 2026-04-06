Milestone 3:

Original plan: We originally planned to analyze London air quality data (daily pollutant measurements for 2024) and combine it with a World Health Organization dataset on air pollution-related deaths.

After receiving feedback on this plan we realized that the integration section of this project and this data would be very difficult so we have decided to revisit the datasets that we are going use. Sticking with the theme of UK air quality we have decided to instead use UK government air quality datasets (ENV02) and UK emissions datasets (ENV01) instead of London air quality data. These two new datasets work better than our previous selections because they both deal with air quality at a country level rather than mixing in city level data like our previous plan. We still plan on including the WHO dataset on air pollution deaths but limiting it only to the UK so that it can be aligned with our other datasets. 

Links to the all the datasets:

-	This data set contains data on the concentrations of major air pollutants as measured by the Automatic Urban and Rural Network (AURN)
https://www.gov.uk/government/statistical-data-sets/env02-air-quality-statistics 
o	https://assets.publishing.service.gov.uk/media/685bba977d72089d1997609b/PM25_Tables_2024.ods 
-	Emissions of PM10 and PM2.5 in the UK
https://www.gov.uk/government/statistics/emissions-of-air-pollutants/emissions-of-air-pollutants-in-the-uk-particulate-matter-pm10-and-pm25
o	https://assets.publishing.service.gov.uk/media/6983269a13622473b51ca9b2/fig03_particulate_matter_annual_emissions.csv
o	https://assets.publishing.service.gov.uk/media/698326c15a7e802e96d343c4/fig04_pm10_key_emission_sources.csv 
-	The WHO air pollution deaths source
https://www.who.int/data/gho/data/indicators/indicator-details/GHO/ambient-air-pollution-attributable-deaths

We have also updated our research questions to align more with our new datasets. 
-	How have PM2.5 concentrations changed over time in the UK?
-	What is the relationship between total particulate emissions and PM2.5 concentrations?
-	Which emission sources contribute most to changes in air quality over time?
Timeline: 

1.	Data Collection & Acquisition 
In our original plan we aimed to collect all the required data but since we are switching datasets, we have to start most of that process over. This includes reading in and then checking the integrity by hashing (with SHA-256) the PM2.5 air quality dataset (ENV02) and the emissions datasets from UK government sources. We plan on documenting all steps and creating a reproduceable way of acquiring the data with the python “requests” library. 

Roles and Completion Estimates: Surya will mainly work on this section and plan to complete it by April 5th. 

2.	Data Cleaning & Integration
Once the data is collected, we will begin parsing and cleaning the datasets. This includes handling the .ods file format and extracting relevant tables. All datasets will then be merged into a singular data frame with clearly defined variables (year, pollutant concentration, emissions). Then we will look into adding the WHO dataset and joining by year in order to compare the deaths due to air pollution with the amount of air pollution in the UK. This will allow us to start making graphs and other visualizations based on this new integrated data. We will look through the data for missing or inconsistent values and check the quality of the data. 

Roles and Completion Estimates: Jonah will work on this section, and we plan on completing it by April 12th

3.	Data Analysis and Visualization 
We will then perform data analysis to address our research questions. This includes analyzing long-term trends in PM2.5 concentrations and emissions, as well as examining the relationship between emissions and air quality. We plan on creating visualizations to support the analysis, including a line graph showing emission and pollutants trends over time, a scatter plot illustrating the relationship between emissions and PM2.5 levels, and a bar chart displaying emissions by source. We will also calculate summary statistics and correlations to quantify relationships in the data. 
After this initial analysis, if we plan to include data about the WHO air pollution deaths and create some graphs such as a comparison bar graph representing the percentage of UK citizens that died due to air pollution compared with the number of pollutants in the air. All of these visualizations and statistics directly tie into our research questions and all interpretations and insights will be documented.

Roles and Completion Estimates: We will both work on this section, taking different graphs each and combining them in the final report. We will work together to find answers to our research questions through these graphs and add them to the report.
We plan on completing this section by April 19th

4.	Reproducibility and Documentation
After completing the analysis and visualizations we plan on spending time editing our report in order to make sure that someone reading our report will have all the tools necessary in order to reproduce our work.

Roles and Completion Estimates: We both plan on working on this section together, documenting any changes we made and adding them to the report. Then we will check that our processes line up and can be easily reproduced by someone else.

Changes:
We made significant changes to our project plan since the last milestone including switching which datasets we plan on using as well as our overall research goal. The main ideas are staying the same in regard to air quality measurements and analytical processes such as loading in, cleaning and creating visualizations for the data. We also changed our timeline since it didn’t clearly define roles, and we are working with new data. Our new timeline accurately reflects what our project is and who will be working on what.

Challenges: 
We ran into some initial challenges when trying to process and hash the data. For example, the pm25 data frame starts at row 2 because there was a repeat in the header, so the first row needed to be cut. There are also a lot of missing values, such as in the “measurement frequency” column in the pm25 data frame but they aren’t just missing with NaN, they are replaced by “[z]” since that is how the data was formatted before so a simple drop_na isn’t going to get rid of them. We plan on either renaming these values to something more informative or dropping the column entirely if we feel like it isn’t needed. 

Jonah Summary: Found and updated the links to the new datasets required for the project as well as helped develop a plan for how to use the datasets in the analysis stage. Outlined and implemented the new timeline and made comparisons with the old plan. Started the process of cleaning and integrating the data that Surya implemented and hashed. Since the csv file version of the pm25 was still formatted as an excel file, I processed the data into a clean data frame and removed and updated any columns that were not needed/fit for analysis. For example, I updated the emissions data frame which included both pm10 and pm25 data to include only pm25 data since that is the data that is available in the other csv file.

Surya Summary: 
