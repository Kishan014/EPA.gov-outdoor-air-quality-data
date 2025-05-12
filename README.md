EPA Outdoor Air Quaility Data
https://www.epa.gov/outdoor-air-quality-data/

Overview
This project is a complete end-to-end data engineering pipeline that extracts, processes, and analyzes EPA's historical and real time data for daily air quality summary statistics for the criteria pollutants by monitor. You can get data for specific monitors or all monitors in a city, county, or state.  
We will implement a batch processing architecture to collect historical data and we will specificly analyze the CO pollutant for this project. The raw data will be stored in a data lake (Google Cloud Storage) in the form of csv's. Next the data will be moved to a data warehouse (BigQuery) for cleaning,consolidation, and analysis.

Using dbt (data build tool) for data transformation and modeling ensures data quality and consistency. Ultimately, this carefully processed data is transformed into an interactive visualization dashboard using Google Looker Studio, allowing users to query and analyze parking availability in real-time to support travel decisions.

The project uses Apache Airflow for workflow orchestration, implementing a fully automated ELT (Extract, Load, Transform) process to ensure seamless integration of data throughout its lifecycle from collection to analysis.

The final output of this project is a comprehensive interactive dashboard that enables users to:

View real-time available parking spaces across Singapore
Analyze parking usage trends across different time periods and areas
Predict parking difficulty at specific times and locations based on historical data
Optimize trip planning and reduce time spent searching for parking spaces
Through this project, I hope to not only solve personal frustrations with driving, but also provide a valuable reference tool for other drivers, while demonstrating the application of modern data engineering techniques in solving real-life problems.
