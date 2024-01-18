/*
Creates a trigger that resets the attribute `valid_email`
only when the `email` has been changed.
*/

-- create a trigger that resets (set to 0) `valid_email` column
-- of table `users` if and after column `email` is changed.
DELIMITER $$ ;
CREATE TRIGGER reset_vallid_email
BEFORE UPDATE ON users FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END $$
DELIMITER ; $$
