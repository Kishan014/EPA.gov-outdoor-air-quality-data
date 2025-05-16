SELECT
  date_cleaned AS date,
  state,
  co_level_standardized AS co_level,
  data_source
FROM
  {{ ref('air_quality_table') }}
ORDER BY
  date_cleaned