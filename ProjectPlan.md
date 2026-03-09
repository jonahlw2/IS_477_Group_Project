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

