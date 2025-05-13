# EPA Outdoor Air Quality Data
https://www.epa.gov/outdoor-air-quality-data/

## Overview
This project is a complete end-to-end data engineering pipeline that extracts, processes, and analyzes EPA's historical and real time data for daily air quality summary statistics for the criteria pollutants to monitor.

The final output of this project is a comprehensive interactive dashboard that enables users to:

* View historical CO pollutant data by state, county, and local sites
* Analyze pollutant trends across different time periods and areas
* Understand trends of improvement or deterioration by filtering for sites with the best and worst pollution

## Tech Stack

* **Visualization: Looker Studio**  
  Looker Studio (formerly Google Data Studio) provides rich data visualization capabilities, directly connecting to BigQuery data sources to create interactive dashboards. Through a drag-and-drop interface and custom charts, it displays key metrics and trends in parking availability, allowing end users to easily understand and utilize data insights to make informed parking decisions.

* **Containerization Platform: Docker**  
  Docker provides standardized container environments, ensuring consistent project execution across different infrastructure. By encapsulating components (like Kafka, Airflow, etc.) into independent containers, it greatly simplifies deployment and achieves perfect consistency between development and production environments, reducing the complexity of environment configuration.

* **Cloud Platform: Google Cloud Platform (GCP)**  
  GCP, as a global leading cloud service provider, offers complete infrastructure and service support. This project leverages GCP's high reliability, globally distributed architecture, and powerful data processing capabilities to build a scalable and cost-effective cloud-native solution, particularly suitable for developing and running data-intensive applications.

* **Infrastructure as Code: Terraform**  
  Terraform enables programmatic management of infrastructure through declarative configuration files that automate the creation and management of GCP resources, including storage buckets, BigQuery datasets, and compute instances. This ensures repeatable infrastructure deployment, version control, and consistency, greatly improving development efficiency and system stability.

* **Workflow Orchestration: Apache Airflow**  
  Airflow serves as a powerful workflow orchestration tool responsible for scheduling and monitoring the entire data pipeline. Through Python-defined DAGs (Directed Acyclic Graphs), it automates the execution of data extraction, processing, and loading tasks, and provides a rich monitoring interface and failure retry mechanisms, ensuring data processing reliability and visualization.

* **Data Transformation: dbt Cloud**  
  dbt (data build tool) Cloud offers powerful data transformation and modeling capabilities, implementing structured transformations in the data warehouse through SQL and Git version control. dbt's modular design and testing framework ensure data quality and consistency, allowing data analysts to focus on business logic rather than technical implementation.

* **Storage & Warehousing: Google Cloud Storage (GCS), BigQuery**  
  GCS serves as a high-performance object storage service, providing data lake functionality for storing raw and processed data. BigQuery, as a serverless data warehouse, offers millisecond-level query performance and PB-level data processing capabilities, achieving cost-effective large-scale data analysis, with its no-provisioning feature allowing systems to scale automatically according to demand.

## Project Architecture 

![image](https://github.com/user-attachments/assets/42a52d29-8cc2-4285-b94d-ed5105399a79)

![image](https://github.com/user-attachments/assets/404d464f-6919-4365-8f6f-48f828dcee81)


