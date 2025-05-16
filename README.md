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


## Project Structure

EPAPipeline
├─ airflow-docker
│  ├─ csv
│  │  ├─ CO_2024_Alabama.csv
│  │  ├─ CO_2024_Alaska.csv
│  │  ├─ CO_2024_Arizona.csv
│  │  ├─ CO_2024_Arkansas.csv
│  │  ├─ CO_2024_California.csv
│  │  ├─ CO_2024_Colorado.csv
│  │  ├─ CO_2024_DOC.csv
│  │  ├─ CO_2024_Florida.csv
│  │  ├─ CO_2024_Georgia.csv
│  │  ├─ CO_2024_Hawaii.csv
│  │  ├─ CO_2024_Idaho.csv
│  │  ├─ CO_2024_Illinois.csv
│  │  ├─ CO_2024_Indiana.csv
│  │  ├─ CO_2024_Iowa.csv
│  │  ├─ CO_2024_Kentucky.csv
│  │  ├─ CO_2024_Louisiana.csv
│  │  ├─ CO_2024_Maine.csv
│  │  ├─ CO_2024_Maryland.csv
│  │  ├─ CO_2024_Massachusetts.csv
│  │  ├─ CO_2024_Michigan.csv
│  │  ├─ CO_2024_Minnesota.csv
│  │  ├─ CO_2024_Mississippi.csv
│  │  ├─ CO_2024_Missouri.csv
│  │  ├─ CO_2024_Montana.csv
│  │  ├─ CO_2024_Nebraska.csv
│  │  ├─ CO_2024_New_Hampshire.csv
│  │  ├─ CO_2024_New_Jersey.csv
│  │  ├─ CO_2024_New_Mexico.csv
│  │  ├─ CO_2024_New_York.csv
│  │  ├─ CO_2024_North_Carolina.csv
│  │  ├─ CO_2024_North_Dakota.csv
│  │  ├─ CO_2024_Ohio.csv
│  │  ├─ CO_2024_Oklahoma.csv
│  │  ├─ CO_2024_Oregon.csv
│  │  ├─ CO_2024_Pennsylvania.csv
│  │  ├─ CO_2024_Puerto_Rico.csv
│  │  ├─ CO_2024_Rhode_Island.csv
│  │  ├─ CO_2024_South_Carolina.csv
│  │  ├─ CO_2024_South_Dakota.csv
│  │  ├─ CO_2024_Tennessee.csv
│  │  ├─ CO_2024_Texas.csv
│  │  ├─ CO_2024_Utah.csv
│  │  ├─ CO_2024_Vermont.csv
│  │  ├─ CO_2024_Virginia.csv
│  │  ├─ CO_2024_Washington.csv
│  │  ├─ CO_2024_West_Virginia.csv
│  │  ├─ CO_2024_Wisconsin.csv
│  │  ├─ CO_2024_Wyoming.csv
│  │  ├─ CO_2025_Arkansas.csv
│  │  ├─ CO_2025_Colorado.csv
│  │  ├─ CO_2025_Georgia.csv
│  │  ├─ CO_2025_Illinois.csv
│  │  ├─ CO_2025_Indiana.csv
│  │  └─ CO_2025_Iowa.csv
│  ├─ dags
│  │  ├─ csv_to_gcs.py
│  │  ├─ gcs_to_bigquery.py
│  │  └─ __pycache__
│  │     ├─ csv_to_gcs.cpython-312.pyc
│  │     └─ gcs_to_bigquery.cpython-312.pyc
│  ├─ dbt
│  │  └─ air_quality_dbt
│  │     ├─ .user.yml
│  │     ├─ dbt_project.yml
│  │     ├─ logs
│  │     │  └─ dbt.log
│  │     ├─ models
│  │     │  ├─ air_quality_table.sql
│  │     │  ├─ air_quality_time_series.sql
│  │     │  ├─ co_level_summary.sql
│  │     │  ├─ schema.yml
│  │     │  ├─ site_level_metrics.sql
│  │     │  └─ sources.yml
│  │     ├─ profiles.yml
│  │     └─ target
│  │        ├─ compiled
│  │        │  └─ air_quality_dbt
│  │        │     └─ models
│  │        │        ├─ air_quality_table.sql
│  │        │        ├─ air_quality_time_series.sql
│  │        │        ├─ co_level_summary.sql
│  │        │        ├─ schema.yml
│  │        │        │  ├─ accepted_values_air_quality_table_co_level_standardized___0.sql
│  │        │        │  ├─ not_null_air_quality_table_co_level_standardized.sql
│  │        │        │  ├─ not_null_air_quality_table_date_cleaned.sql
│  │        │        │  ├─ not_null_air_quality_table_site_id.sql
│  │        │        │  └─ not_null_air_quality_table_state.sql
│  │        │        └─ site_level_metrics.sql
│  │        ├─ graph.gpickle
│  │        ├─ graph_summary.json
│  │        ├─ manifest.json
│  │        ├─ partial_parse.msgpack
│  │        ├─ run
│  │        │  └─ air_quality_dbt
│  │        │     └─ models
│  │        │        ├─ air_quality_table.sql
│  │        │        ├─ air_quality_time_series.sql
│  │        │        ├─ co_level_summary.sql
│  │        │        ├─ schema.yml
│  │        │        │  ├─ accepted_values_air_quality_table_co_level_standardized___0.sql
│  │        │        │  ├─ not_null_air_quality_table_co_level_standardized.sql
│  │        │        │  ├─ not_null_air_quality_table_date_cleaned.sql
│  │        │        │  ├─ not_null_air_quality_table_site_id.sql
│  │        │        │  └─ not_null_air_quality_table_state.sql
│  │        │        └─ site_level_metrics.sql
│  │        ├─ run_results.json
│  │        └─ semantic_manifest.json
│  ├─ docker-compose.yaml
│  ├─ docker-compose.yaml.bak
│  ├─ Dockerfile
│  ├─ gcp-key.json
│  ├─ netstat
│  ├─ Project Architecture.png
│  └─ requirements.txt
├─ Data
│  ├─ CO_2024_Alabama.csv
│  ├─ CO_2024_Alaska.csv
│  ├─ CO_2024_Arizona.csv
│  ├─ CO_2024_Arkansas.csv
│  ├─ CO_2024_California.csv
│  ├─ CO_2024_Colorado.csv
│  ├─ CO_2024_DOC.csv
│  ├─ CO_2024_Florida.csv
│  ├─ CO_2024_Georgia.csv
│  ├─ CO_2024_Hawaii.csv
│  ├─ CO_2024_Idaho.csv
│  ├─ CO_2024_Illinois.csv
│  ├─ CO_2024_Indiana.csv
│  ├─ CO_2024_Iowa.csv
│  ├─ CO_2024_Kentucky.csv
│  ├─ CO_2024_Louisiana.csv
│  ├─ CO_2024_Maine.csv
│  ├─ CO_2024_Maryland.csv
│  ├─ CO_2024_Massachusetts.csv
│  ├─ CO_2024_Michigan.csv
│  ├─ CO_2024_Minnesota.csv
│  ├─ CO_2024_Mississippi.csv
│  ├─ CO_2024_Missouri.csv
│  ├─ CO_2024_Montana.csv
│  ├─ CO_2024_Nebraska.csv
│  ├─ CO_2024_New_Hampshire.csv
│  ├─ CO_2024_New_Jersey.csv
│  ├─ CO_2024_New_Mexico.csv
│  ├─ CO_2024_New_York.csv
│  ├─ CO_2024_North_Carolina.csv
│  ├─ CO_2024_North_Dakota.csv
│  ├─ CO_2024_Ohio.csv
│  ├─ CO_2024_Oklahoma.csv
│  ├─ CO_2024_Oregon.csv
│  ├─ CO_2024_Pennsylvania.csv
│  ├─ CO_2024_Puerto_Rico.csv
│  ├─ CO_2024_Rhode_Island.csv
│  ├─ CO_2024_South_Carolina.csv
│  ├─ CO_2024_South_Dakota.csv
│  ├─ CO_2024_Tennessee.csv
│  ├─ CO_2024_Texas.csv
│  ├─ CO_2024_Utah.csv
│  ├─ CO_2024_Vermont.csv
│  ├─ CO_2024_Virginia.csv
│  ├─ CO_2024_Washington.csv
│  ├─ CO_2024_West_Virginia.csv
│  ├─ CO_2024_Wisconsin.csv
│  ├─ CO_2024_Wyoming.csv
│  ├─ CO_2025_Arkansas.csv
│  ├─ CO_2025_Colorado.csv
│  ├─ CO_2025_Georgia.csv
│  ├─ CO_2025_Illinois.csv
│  ├─ CO_2025_Indiana.csv
│  └─ CO_2025_Iowa.csv
└─ terraform
   ├─ air-quality-pipeline
   │  └─ terraform
   │     ├─ .terraform
   │     │  └─ providers
   │     │     └─ registry.terraform.io
   │     │        └─ hashicorp
   │     │           └─ google
   │     │              └─ 6.27.0
   │     │                 └─ windows_amd64
   │     │                    ├─ LICENSE.txt
   │     │                    └─ terraform-provider-google_v6.27.0_x5.exe
   │     ├─ .terraform.lock.hcl
   │     ├─ main.tf
   │     ├─ terraform.tfstate
   │     └─ terraform.tfstate.backup
   ├─ terraform.exe
   └─ terraform_1.11.3_windows_amd64
      └─ LICENSE.txt

![image](https://github.com/user-attachments/assets/404d464f-6919-4365-8f6f-48f828dcee81)


