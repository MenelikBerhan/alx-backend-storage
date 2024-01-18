/*
Creates a trigger that decreases the quantity of an item after adding a new order.
*/

-- create a trigger that decreases `quantity` column value of table `items`,
-- when a new row is inserted in `orders` table.
CREATE TRIGGER update_stock
AFTER INSERT ON orders FOR EACH ROW
    UPDATE items SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
