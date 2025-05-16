
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

