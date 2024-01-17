/* Creates a table `users` following these requirements:

With these attributes:
    id, integer, never null, auto increment and primary key
    email, string (255 characters), never null and unique
    name, string (255 characters)
    country, enumeration of countries: US, CO and TN, never null
If the table already exists, the script will not fail
The script can be executed on any database
*/

-- creates a table with the above requirements
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL
);
