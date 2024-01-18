/*
Creates a stored procedure 'ComputeAverageScoreForUser' that computes
and store the average score for a student.
Procedure ComputeAverageScoreForUser is taking 1 input:
  'user_id', a 'users.id' value (assumed to be linked to an existing user)
*/

-- create a stored procedure with the above specifications
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
  -- calculate average score and store it in 'avg_score' variable
  -- used 'c.user_id' to prevent the selection of all rows when using 'user_id = user_id'
  SELECT AVG(score) INTO @avg_score FROM corrections c WHERE c.user_id = user_id;
  -- update average_score of user in 'users' table
  UPDATE users SET average_score = @avg_score WHERE id = user_id;
END$$
DELIMITER ;
