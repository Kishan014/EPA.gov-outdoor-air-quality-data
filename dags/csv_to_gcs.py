from airflow import DAG
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from datetime import datetime

with DAG(
    dag_id='csv_to_gcs',
    start_date=datetime(2025, 4, 21),
    schedule_interval=None,
    catchup=False,
) as dag:

    upload_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_to_gcs',
        src='/opt/airflow/csv/*.csv',  # Wildcard to match all .csv files
        dst='raw/2025-04-21/',        # Directory in GCS (with trailing slash)
        bucket='co-air-quality-data-lake',
        gcp_conn_id='google_cloud_default',
    )