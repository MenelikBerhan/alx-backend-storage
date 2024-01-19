/*
 Creates a stored procedure `ComputeAverageWeightedScoreForUsers`
 that computes and store the average weighted score for all students.
 */
-- create a stored procedure with above specification
DELIMITER $
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
   -- find the maxium `id` value from users
   SELECT MAX(id) INTO @max_user_id FROM users;

   SET @user_id = 1;

   -- loop from 1 to max user_id (inclusive), calculating
   -- and setting weighted average score for each user_id
   WHILE @user_id <= @max_user_id DO
      -- calculate weighted average and store in variable
      SELECT
         (sum(weight * score) / sum(weight)) INTO @calculated_weighted_avg
      FROM
         (
            SELECT
               p.weight,
               c.score
            FROM
               users u,
               projects p,
               corrections c
            WHERE
               u.id = @user_id
               AND u.id = c.user_id
               AND p.id = c.project_id
         ) AS weights_table;
      
       -- IF not null, store calculated weighted average in `users` table
      IF @calculated_weighted_avg IS NOT NULL THEN
         UPDATE
            users
         SET
            average_score = @calculated_weighted_avg
         WHERE
            id = @user_id;
      END IF;

      SET @user_id = @user_id  + 1;
   END WHILE;

END$
DELIMITER ;
