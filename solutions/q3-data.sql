use `sales`;

ALTER TABLE `closed_deals`
    ADD COLUMN `customer_name` VARCHAR(100);

INSERT INTO `salespersons` 
    (`name`, `commission_rate`)
VALUES
    ('Alan Tay', '0.5'),
    ('Mandy Wikes', '0.009');

INSERT INTO `closed_deals` 
    (`deal_size`, `customer_name`, `product_name`, `salesperson_id`)
VALUES
    ('3000000', 'Phua Chua Kang', 'SuperComputer', '3'),
    ('4600000', 'Elon Musk', 'AI System', '4');

