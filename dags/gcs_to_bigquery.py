from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    'gcs_to_bigquery',
    default_args=default_args,
    description='Load data from GCS to BigQuery and transform with dbt',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
) as dag:
    # Step 1: Create an external table pointing to all state CSV files in the correct folder
    create_external_table = BigQueryInsertJobOperator(
        task_id='create_external_table',
        gcp_conn_id='google_cloud_default',
        configuration={
            "query": {
                "query": """
                CREATE OR REPLACE EXTERNAL TABLE `airqualitydata-455321.co_air_quality.external_raw`
                OPTIONS (
                  format = 'CSV',
                  uris = ['gs://co-air-quality-data-lake/raw/2025-04-21/*.csv'],
                  skip_leading_rows = 1
                );
                """,
                "useLegacySql": False,
            }
        },
    )
    
    # Step 2: Create a temp table from the external table
    create_temp_table = BigQueryInsertJobOperator(
        task_id='create_temp_table',
        gcp_conn_id='google_cloud_default',
        configuration={
            "query": {
                "query": """
                CREATE OR REPLACE TABLE `airqualitydata-455321.co_air_quality.temp_raw` AS
                SELECT * FROM `airqualitydata-455321.co_air_quality.external_raw`;
                """,
                "useLegacySql": False,
            }
        },
    )
    
    # Step 3: Load all data into co_2024_raw
    transform_and_load = BigQueryInsertJobOperator(
        task_id='transform_and_load',
        gcp_conn_id='google_cloud_default',
        configuration={
            "query": {
                "query": """
                -- Clear existing data
                TRUNCATE TABLE `airqualitydata-455321.co_air_quality.co_2024_raw`;
                
                -- Load all state data
                INSERT INTO `airqualitydata-455321.co_air_quality.co_2024_raw`
                SELECT
                  Date,
                  Source,
                  CAST(Site_ID AS STRING) as Site_ID,
                  POC,
                  Daily_Max_8_hour_CO_Concentration,
                  Units,
                  Daily_AQI_Value,
                  Local_Site_Name,
                  Daily_Obs_Count as Daily_Obs_Percent_Complete,
                  CAST(AQS_Parameter_Code AS STRING) as AQS_Parameter_Code,
                  AQS_Parameter_Description,
                  CAST(Method_Code AS STRING) as Method_Code,
                  CAST(CBSA_Code AS STRING) as CBSA_Code,
                  CBSA_Name,
                  CAST(State_FIPS_Code AS STRING) as State_FIPS_Code,
                  State,
                  CAST(County_FIPS_Code AS STRING) as County_FIPS_Code,
                  County,
                  Site_Latitude,
                  Site_Longitude
                FROM `airqualitydata-455321.co_air_quality.temp_raw`;
                """,
                "useLegacySql": False,
            }
        },
    )
    
    # Step 4: Update the dbt model to select only the required columns - with proper Jinja escaping
    fix_dbt_model = BashOperator(
        task_id='fix_dbt_model',
        bash_command="""
        cat > /opt/airflow/dbt/air_quality_dbt/models/air_quality_table.sql << 'EOT'
{% raw %}
{{ config(materialized='table') }}
SELECT
  Date as date,
  DATE(Date) AS date_cleaned,
  CAST(Site_ID AS STRING) as site_id,
  Daily_Max_8_hour_CO_Concentration as co_level,
  CASE
    WHEN LOWER(Units) = 'ppb' THEN Daily_Max_8_hour_CO_Concentration / 1000
    ELSE Daily_Max_8_hour_CO_Concentration
  END AS co_level_standardized,
  Units as unit,
  Daily_AQI_Value as aqi_value,
  Local_Site_Name as location_name,
  Daily_Obs_Percent_Complete as obs_count,
  CBSA_Name as cbsa_name,
  State as state,
  County as county,
  Site_Latitude as latitude,
  Site_Longitude as longitude
FROM
  {{ source('co_air_quality', 'co_2024_raw') }}
WHERE
  Daily_Max_8_hour_CO_Concentration IS NOT NULL
  AND Daily_Max_8_hour_CO_Concentration >= 0
  AND Date IS NOT NULL
  AND State IS NOT NULL
{% endraw %}
EOT
        """,
    )
    
    # Step 5: Add a site-level metrics model - with proper Jinja escaping
    create_site_analysis_model = BashOperator(
        task_id='create_site_analysis_model',
        bash_command="""
        cat > /opt/airflow/dbt/air_quality_dbt/models/site_level_metrics.sql << 'EOT'
{% raw %}
{{ config(materialized='table') }}
SELECT
  state,
  location_name,
  site_id,
  county,
  cbsa_name,
  COUNT(*) AS measurement_count,
  AVG(co_level) AS avg_co_level,
  MAX(co_level) AS max_co_level,
  MIN(co_level) AS min_co_level,
  STDDEV(co_level) AS stddev_co_level,
  AVG(aqi_value) AS avg_aqi_value,
  MIN(date_cleaned) AS first_measurement_date,
  MAX(date_cleaned) AS last_measurement_date,
  latitude,
  longitude
FROM
  {{ ref('air_quality_table') }}
GROUP BY
  state, location_name, site_id, county, cbsa_name, latitude, longitude
{% endraw %}
EOT
        """,
    )
    
    # Step 6: Run dbt to execute the transformations
    run_dbt = BashOperator(
        task_id='run_dbt',
        bash_command='export GOOGLE_APPLICATION_CREDENTIALS=/opt/airflow/gcp-key.json && cd /opt/airflow/dbt/air_quality_dbt && /home/airflow/.local/bin/dbt run && /home/airflow/.local/bin/dbt test',
    )

    # Define the workflow sequence
    create_external_table >> create_temp_table >> transform_and_load >> fix_dbt_model >> create_site_analysis_model >> run_dbt