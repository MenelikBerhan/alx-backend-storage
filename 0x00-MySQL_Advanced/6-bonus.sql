/*
Creates a stored procedure 'AddBonus' that adds a new correction for a student.
Procedure AddBonus is taking 3 inputs (in this order):
    'user_id', a users.id value (assuming user_id is linked to an existing user)
    'project_name', a new or already existing project - if no projects.name found in the table, it will be created
    'score', the score value for the correction.
*/

-- create a stored procedure with the above specifications
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name varchar(255), IN score INT)
BEGIN
  DECLARE project_id INT;
  -- get id of project with 'project_name' and set it to 'project_id' variable.
  -- If no project with 'project_name' exists, 'project_id' will be set to NULL.
  SELECT id INTO project_id FROM projects WHERE name = project_name;

  -- insert a row in `projects` table if there is no entry for 'project_name'
  -- is found, then store id in 'project_id' variable
  IF project_id IS NULL THEN
    INSERT INTO  projects (name) VALUES (project_name);
    SELECT id INTO project_id FROM projects WHERE name = project_name;
  END IF;

  -- insert a new row in `corrections` table
  INSERT INTO  corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END$$
DELIMITER ;
