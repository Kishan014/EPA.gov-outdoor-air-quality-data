SELECT
  date_cleaned AS date,
  state,
  AVG(co_level_standardized) AS avg_co_level,
  MAX(co_level_standardized) AS max_co_level,
  MIN(co_level_standardized) AS min_co_level,
  COUNT(*) AS total_measurements
FROM
  {{ ref('air_quality_table') }}
GROUP BY
  date_cleaned,
  state