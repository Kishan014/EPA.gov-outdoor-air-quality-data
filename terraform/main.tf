provider "google" {
  project = "airqualitydata-455321"
  region  = "us-central1"
}

resource "google_storage_bucket" "data_lake" {
  name          = "co-air-quality-data-lake"
  location      = "US"
  force_destroy = false

  labels = {
    environment = "production"
  }
}

resource "google_bigquery_dataset" "data_warehouse" {
  dataset_id = "co_air_quality"
  project    = "airqualitydata-455321"
  location   = "US"

  labels = {
    environment = "production"
  }
}

resource "google_bigquery_table" "co_measurements" {
  dataset_id = google_bigquery_dataset.data_warehouse.dataset_id
  table_id   = "co_measurements"

  schema = jsonencode([
    { "name": "date", "type": "TIMESTAMP" },
    { "name": "location", "type": "STRING" },
    { "name": "county", "type": "STRING" },
    { "name": "co_level", "type": "FLOAT" }
  ])
}