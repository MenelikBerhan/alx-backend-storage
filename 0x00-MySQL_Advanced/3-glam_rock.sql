/*
Lists all bands with 'Glam rock' as their main style, ranked by their longevity.
*/

-- from table `metal_bands`, select `band_name` columns with 'Glam rock' style and
-- calculate `lifespan` column by using `formed` and `split` column values,
-- then rank result by lifespan in descending order.
SELECT
    band_name,
    IF(split IS NOT NULL, split - formed, 2022 - formed) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
