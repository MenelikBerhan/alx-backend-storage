/*
 Creates a stored procedure `ComputeAverageWeightedScoreForUser` that
 computes and store the average weighted score for a student.
 
 Input: `user_id`, a `users.id` value (assumed to be linked to an existing `users`)
 */
-- create a stored procedure with above specification
DELIMITER $
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
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
            u.id = user_id
            AND u.id = c.user_id
            AND p.id = c.project_id
      ) AS weights_table;
   
   -- store calculated weighted average in `users` table
   UPDATE
      users
   SET
      average_score = @calculated_weighted_avg
   WHERE
      id = user_id;
END$
DELIMITER ;
