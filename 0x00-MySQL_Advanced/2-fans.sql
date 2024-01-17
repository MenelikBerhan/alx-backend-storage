/*
Ranks country origins of bands, ordered by the number of (non-unique) fans.
*/

-- from table `metal_bands`, select `origin` columns and
-- display total non-unique number of fans ordered decendingly by no. of fans
SELECT origin, SUM(fans) as nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
