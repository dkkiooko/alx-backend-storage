-- make a trigger to buy an item
CREATE TRIGGER ItemBought
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
