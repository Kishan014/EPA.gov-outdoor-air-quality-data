EPA Outdoor Air Quaility Data
https://www.epa.gov/outdoor-air-quality-data/ 

Overview
This project is a complete end-to-end data engineering pipeline that extracts, processes, and analyzes EPA's historical and real time data for daily air quality summary statistics for the criteria pollutants by monitor. Data for specific monitors or all monitors in a city, county, or state can be found of the EPA's outdoor air quality site or API. We will implement a batch processing architecture to collect historical data and we will specificly analyze the CO pollutant for this project. The raw data will be stored in a data lake (Google Cloud Storage) in the form of csv's. Next the data will be moved into an data warehouse (BigQuery) for cleaning, consolidation, and analysis. This project will use dbt (data build tool) for data transformation and modeling ensures data quality and consistency, in addition to creating specific tables for more streamlined analysis. This project will utalize Apache Airflow for workflow orchestration, implementing a fully automated ELT (Extract, Load, Transform) process to ensure seamless integration of data throughout its lifecycle from collection to analysis. Ultimately, this carefully processed data is transformed into an interactive visualization dashboard using Google Looker Studio, allowing users to query and analyze pollution data.

The final output of this project is a comprehensive interactive dashboard that enables users to:

View historical CO pollutant data by state, county, and local sites
Analyze pollutant trends across different time periods and areas
Understand trends of improvment or deteration by filterting for sites with the best and worst pollution
This project will give researchers a better understanding of CO pollution which will allow better research of State and municipality policy to improve pollution standards.
