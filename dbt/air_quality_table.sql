
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

