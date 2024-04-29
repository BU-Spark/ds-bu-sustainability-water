# BU Sustainability: Water Filling Stations Team B
Team Members: Marilyn Risinger (marilynr@bu.edu), Allison Lu (alu8@bu.edu), Katherine Deng (kdeng@bu.edu), Grace Van Sciver (gracevs@bu.edu), Xikun Feng (fengxk@bu.edu), Matthew Wang (mattw24@bu.edu)

This repository hosts a software framework designed to identify optimal locations for new water filling stations on Boston University's Charles River Campus. The project leverages various data sources from Boston University to generate a prioritized list of potential sites, each evaluated based on its significance in meeting the campus's hydration needs. Additionally, the framework allows users to input a priority factor of their choice, enabling them to obtain a customized list of locations that aligns with their specific preferences and priorities for installing new water filling stations.

## Project Description
The Boston University Sustainability project focuses on strategically installing water bottle filling stations across the campus to mitigate the environmental impact of single-use plastic bottles. With the goal of significantly reducing plastic waste, the project aims to identify key locations for new stations based on various factors such as foot traffic, proximity to alternative water sources, and building features.

Existing infrastructure, including aging drinking fountains, serves as the foundation for the project's analysis. By evaluating current utilization and effectiveness of existing filling stations, the team recognized the need for additional installations to meet the growing demand and encourage sustainable practices.

Through rigorous data collection and integration, the team compiled datasets encompassing foot traffic patterns, building infrastructure details, and the inventory of known filling stations. Leveraging this information, a weighted scoring system was developed to prioritize potential installation locations. Factors such as foot traffic volume and accessibility to plumbing infrastructure were meticulously considered to ensure the selection of optimal sites.

The project culminated in the creation of a prioritized list of locations deemed most suitable for hosting new water filling stations. This list, derived from comprehensive analysis and careful consideration of various factors, serves as a roadmap for BU Sustainability to strategically deploy new stations and promote campus-wide adoption of sustainable practices.

**Our final prioritized list that includes all locations in prioritized order of installment is found at [final_prioritized_list.csv](final_prioritized_list.csv)**


## Key Questions Answered
**1. How many students and employees are impacted by each water filling station in the current inventory?**

We conducted an analysis on the existing water filling stations across Boston University's Charles River Campus, utilizing WiFi density data as a proxy for foot traffic. Our findings indicate that approximately 33.4% of students and employees are impacted daily by these stations, meaning that roughly one-third of the campus population accesses locations with available water filling stations each day. A visualization of this is available in the project_code.ipynb file.

**2. Establish a full list of factors and criteria for the installation of new filling stations**
We developed a comprehensive set of factors to guide the installation of new water filling stations:

**Foot Traffic:** Measured by WiFi density, this indicates the daily average number of people at each campus location.
**Number of Existing Stations:** Counts the filling stations already in place at various locations.
**Building Type:** Includes categories such as academic, residential, administrative, student support, athletic, research, parking, and commercial buildings.
**Air Conditioning:** Identifies whether locations are equipped with air conditioning.
**Distance to Closest Station:** Calculated from density data, this measures the proximity of each campus location to the nearest existing filling station.

Each factor is weighted according to its importance in determining the prioritization for new installations. The base project involves weights assigned by our team and our client, while the extension project allows users to prioritize a factor of their choice, adjusting the weights accordingly to influence the final prioritized installation list.

**3. A geospatial map of new/proposed water filling stations highlighted by priority**

Using Google Maps, we have created an interactive map to be able to view the top 40 proposed locations for new installations of water filling stations. On this map, each location is highlighted by priority and has a description of where exactly at each address a new water filling station is proposed to be installed.

[Click here for the interactive geospatial map](https://www.google.com/maps/d/u/0/viewer?mid=1M2Y6x05S4kCkZrdMNcw5Biq0rK_sI8c&ll=42.34939202399286%2C-71.10766574597167&z=15)



**4. Establish how many students and employees would have access to each of the proposed new filling stations.**

Our analysis projects significant increases in campus coverage with the installation of new filling stations at prioritized locations:

Top 30 Locations: Increases coverage from 33.4% to 44.9%.

Top 10 Locations: Boosts access from 33.4% to 39.9%.

Top 20 Locations: Raises coverage to 43.1%.

These projections demonstrate the potential to significantly enhance access to water filling stations, supporting the campus community's hydration needs more effectively.

## Data Cleaning and Data Analysis
In our project, we meticulously cleaned and processed various datasets to ensure accuracy and reliability in our analyses. Here's a brief overview of our data cleaning process:

**Setup and Data Importing:** We started by configuring our notebook environment and importing essential datasets. These included data on density metrics (such as foot traffic) and existing water filling stations, sourced from cleaned CSV files on Google Drive.

**Data Cleaning and Preparation:** To ensure data integrity, we filtered out duplicate entries from the density data, retaining only unique address records for analysis. We then merged this cleaned density data with existing filling stations data, enriching station records with latitude and longitude coordinates necessary for distance calculations.

**Handling Missing Data:** To address missing latitude and longitude values, we implemented a method to fill these gaps by borrowing coordinates from nearby records with the same address. This ensured completeness and accuracy in subsequent spatial analyses.

**Distance Calculation Using Haversine Formula:** To quantify the distance of each unique location from the nearest existing water filling station, we utilized the Haversine formula. This algorithm computes the geographical distance between two points on the Earth's surface using their longitude and latitude values.
The calculation of the distance to the nearest existing filling station involved comparing the coordinates of each potential location (derived from the density data) with the coordinates of all existing water filling stations on campus. Using the Haversine formula, we computed the geographical distance between each potential location and all existing stations. By iterating through these calculations, we determined the closest distance for each potential location, effectively creating a new factor—distance to nearest existing filling station—for strategic decision-making in our project.

**Data Enrichment and Exporting:** After calculating distances, we augmented the location data with newly derived 'distance to closest station' values. This enriched dataset was then saved back to a CSV file for further analysis and utilization.

**Visualization of Results:** To visualize the impact of our distance calculations, we sorted and filtered locations by distance and created visualizations, such as bar charts, to highlight areas furthest from existing stations. These visuals facilitated strategic planning discussions and decision-making.




## How to Produce Results
Our current codebase includes [project_code.ipynb](project_code.ipynb), which features a list of the top 30 recommended sites for installing new water filling stations, derived from our base project using predefined weights. This notebook also includes visualizations to illustrate the effects of installing stations at the top 10, 20, or 30 prioritized locations. If you would like to see the full prioritized list of locations from that code, that can be found at [final_prioritized_list.csv](final_prioritized_list.csv).

Additionally, our extension project, housed in [extension_project.ipynb](extension_project.ipynb), allows users to input a factor they wish to prioritize. It generates a tailored list of locations and visualizations that display the impact of installing stations at the top 10, 20, 30 or a chosen number (by the user) of these selected sites. Sample inputs are provided for demonstration, but if you'd like to customize the analysis, here are the steps to run the program with your own inputs:

**1. Download the Files:**
Download [extension_project.ipynb](extension_project.ipynb) and [extension_data.csv](data/extension_data.csv) from the data folder.

**2. Open the Notebook:**
Open extension_project.ipynb using Jupyter Notebook on your computer, through a RedHat environment, or upload it to Google Drive (to use Google Collabs to run it) ** . If using Google Drive, ensure extension_data.csv is also uploaded there.

** I suggest using Google Collabs to run this. If using your own computer with Jupyter Notebook, you will have to have the proper installments on your computer for the program to be able to run.

**3. Configure the Data Path:**
Modify the path_to_data variable at the beginning of the notebook to reflect the path to your extension_data.csv.

**4. Set Your Preferences:**
Assign factor_to_prioritize to the factor you wish to emphasize in the location selection process.
Specify number_proposed_locations to set how many locations from the prioritized list you wish to evaluate. The notebook defaults to visualizing the impact of the top 10, 20, and 30 locations, but you can set this to another number if desired.

**5. Run the Notebook:**
Execute all cells in the notebook, either by running them individually from top to bottom or by using the "Run All" feature.

**6. Review the Outcomes:**
Examine the outputs, including the prioritized list of locations and their projected impacts.
If the results are not as expected, you can adjust the factor_to_prioritize or number_proposed_locations and rerun the relevant sections to explore different scenarios.





## Resources
1. [Inventory of known/existing filling stations](https://docs.google.com/spreadsheets/d/1dlOriaa1WtYOUGU08oml872JZsaB1OSh/edit?usp=drive_link&ouid=108966183029096150159&rtpof=true&sd=true)
2. [Inventory of campus buildings and rooms with kitchens](https://docs.google.com/spreadsheets/d/1wjGc2l0J6_1BAEXtIwVTpCvNiI-47YRE/edit?usp=drive_link&ouid=108966183029096150159&rtpof=true&sd=true)
3. [BU Wifi Data for foot traffic](https://drive.google.com/file/d/15CcnxduK7VtXMfdQytTy3hwTYPzsAlt1/view?usp=drive_link)
4. [BU Floor Descriptions (Useful for foot traffic data)](https://drive.google.com/file/d/1Lnbod-xwY5s3cIzho5kOy8-McGSVLwtW/view?usp=drive_link)
5. [BU High Volume Event spaces](https://docs.google.com/spreadsheets/d/1CpkKEFwkfS80ynrXnw2LlY6I33I2E-Aa/edit?usp=drive_link&ouid=108966183029096150159&rtpof=true&sd=true)
