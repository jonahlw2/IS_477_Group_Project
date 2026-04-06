Overview: Describe the overall goal of your project and your planned approach to achieve it. Explain what you aim to accomplish and outline the main steps or methods you will use to execute the project (max 250 words).

The overall goal of our project is to analyze the air quality in the London area during 2024 using publicly available data on the uk.gov website. Through this analysis we aim to examine different patterns throughout the air quality data and create a timeline to see how the air quality has changed throughout a full calendar year. We will focus specifically on several major pollutants that are commonly used to measure urban air quality and track how their concentrations vary over time. This will help us identify periods of higher or lower pollution levels throughout the year.

We then plan to combine this data analysis with a dataset from the World Health Organization (WHO) that collects data on deaths from air pollution. By comparing pollution levels (based on the air quality from the other dataset) with health impact data, we hope to identify possible relationships between increased pollution levels and higher mortality related to air pollution exposure.  

We will first clean and prepare the data for analysis and then use the Python package pandas to organize and calculate our results. Further along in the project we aim to use another python package such as matplotlib to visulaize our results. The end goal of the project is to find out which pollutants are the most dangerous and show what direction the air quality in London is heading and categorize this information into an easy to read graph. 

Team: Clearly define team member roles and responsibilities.

Each team member will contribute to different parts of the project including data collection, data cleaning, analysis, and visualization.  


Research or Business Question(s): What is/are the question(s) you intend to address? These could be research questions, business questions, or analytical questions you want to answer through data analysis.

The main research questions that we plan to answer are:
- In what direction is the air quality in London headed? Positive or Negative?
- What are the most present pollutants in London air quality?
- What is the mortality rate from air pollutants?
- Which pollutants are the most harmful?
An extra question that may require more than data then we have at the moment is:
- How can we reduce air pollution?

Datasets: Identify and describe the datasets you will use to answer your question(s). You need to use at least two different datasets that complement each other and can be integrated together. (for Group of 3, you are required to choose at least three different datasets!) The datasets should each contribute different but related information needed to address your questions, and they must share common attributes or identifiers that allow you to link them. For example, if one dataset contains demographic information and another contains economic indicators, they should both include geographic codes or time periods that enable meaningful integration.If you need help finding suitable datasets, start by reviewing the list of datasets provided in class. 

The first dataset used for this project will consist of air quality measurements collected from monitoring stations in London, including pollutants such as particulate matter (PM2.5 and PM10), nitrogen dioxide (NO₂), and ozone (O₃). These measurements are recorded daily and provide a detailed view of air pollution levels across the year.These topics will guide the analysis of the datasets and help determine whether pollution levels appear to be improving or worsening over time.

Our second dataset is from the World Health Organization (WHO) and shows the record of ambient air pollution deaths based on factors from different countries. The goal of this dataset is to search for the causes of air pollution deaths in London and compare it with the air quality data in London and see if there is overlap. This dataset contains data such as location, year/time, cause of death, sex, and indicator code. The WHO dataset provides a broader global context that can help explain the health impacts associated with different types of air pollutants.

The goal here is to be able to find a way to combine the datasets or maybe add a third to find out if there is a corellation between different pollutants and deaths.


Constraints: Describe any known limitations or challenges with your datasets or approach. These might include legal or ethical restrictions, unknown data provenance, technical difficulties in processing the data, issues with data completeness, limited temporal or spatial coverage, accessibility barriers, or other relevant concerns that could affect your work.

One of the biggest constraints with dealing with this data is the timeframe. The data from the uk government site hasn't been verified since 2024 which is why we are choosing that data instead of more recent data. Another factor is the the dates matching up between datasets. The WHO dataset was updated in 2024 so it should match up but there are many entries from earlier years that we will need to sort through and see if we can find all of the necessary data. Another factor we need to consider is the completeness of the data. From just a quick glance it looked like there were some missing values so that will need to be dealt with later on. 

The data looks like it is all from verified sources with correct licensing, both government websites. However, differences in how the datasets were collected or reported may create challenges when attempting to directly compare them.

Gaps: Identify any known gaps or areas where you need additional input.
Your plan should anticipate later course topics even if you don’t yet know all the details. It is expected that your plan will evolve over time.

The biggest gaps that we have at the moment is most likely going to be combining the data. We have just recently gone over joins in SQL in class but we do not know how that is going to correlate to python and csv files. Along with that, we have found other data that is in Excel format that may need to be converted to something else if we want to work with it so that will be another challenge later on. This is especially the case as the excel file has multiple tabs which could create confusion. 

Another possible gap is determining the best way to align the time periods and locations between datasets so that meaningful comparisons can be made. If the time periods aren't exact then we could have issues connecting the two datasets by the correct date as we can see issues formatting that. The same is true for locations, "London" and "WC1/WC2 (Central London)" could be difficult to match up and find out exactly where the datasets overlap.

Timeline

Week 1

Tasks:

Finalize the research questions and overall scope of the project

Confirm the datasets we will use, including the UK government air quality data and the WHO mortality data

Look for a possible third dataset if we need one to better connect pollution and health outcomes

Download the datasets and organize all project files

Start reviewing the datasets for missing values, duplicate entries, and formatting issues

Begin standardizing dates, pollutant names, and location names

Description:
During the first week, we will focus on setting up the foundation of the project. This means making sure our research questions are clear, confirming that our datasets are appropriate, and organizing our files so the project is easy to manage. We will also begin the cleaning process early so that we can identify any issues with the data before moving into deeper analysis.

Week 2

Tasks:

Continue cleaning the datasets and documenting any changes we make

Identify the common fields that can be used to connect the datasets

Begin combining the datasets using Python/Pandas or SQL

Check whether the merged data is accurate and useful for answering our research questions

Create any new columns or summary measures needed for later analysis

Description:
The second week will be focused on preparing the data for analysis. After continuing the cleaning process, we will work on integrating the datasets in a meaningful way. Since the datasets may not match perfectly by date, location, or category, this week will also involve testing different ways to connect them and making sure the combined data is reliable enough to use.

Week 3

Tasks:

Analyze trends in London air quality across 2024

Identify which pollutants appear most frequently or at the highest levels

Compare pollution patterns with the mortality-related data

Begin creating graphs and visualizations to present the results

Review the quality of the final dataset and note any limitations

Description:
In the third week, we will begin the main analysis of the project. We will look at pollution trends over time, study which pollutants are most important in the dataset, and compare those findings with the health data. We will also begin creating visualizations to make the results easier to understand and to help us see patterns more clearly.

Week 4

Tasks:

Finalize graphs, tables, and other visual outputs

Complete the written analysis and interpretation of results

Organize the full workflow from data collection to final analysis

Make sure the project is reproducible and clearly documented

Prepare the final report and any presentation materials

Description:
The last week will focus on pulling the full project together. We will finish the analysis, finalize the visuals, and make sure our workflow is organized clearly from beginning to end. We also want to make sure that someone else could understand our process and reproduce our work using the files, code, and documentation we provide.

Responsibilities

Both team members will contribute to all major parts of the project, but each person will take primary responsibility for certain areas. One team member will focus more on the London air quality dataset, including data collection, file organization, and part of the cleaning and analysis. The other team member will focus more on the WHO mortality dataset, metadata, documentation, and checking how well the datasets can be combined. Both team members will work together on integration, interpretation of results, visualization, and the final report.

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
Add roles and completion estimates: We will both work on this section, taking different graphs each and combining them in the final report. We will work together to find answers to our research questions through these graphs and add them to the report.
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
