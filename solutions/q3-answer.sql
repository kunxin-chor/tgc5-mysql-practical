create database `sales`;

use `sales`;

create table `salespersons` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    commission_rate float NOT NULL
);

create table `closed_deals` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    deal_size float NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    salesperson_id INT NOT NULL,
    FOREIGN KEY (`salesperson_id`) REFERENCES `salespersons`(`id`)
);

/* SUPPOSE WE FORGOT TO CREATE THE FK OR WE WANT TO PUT IN LATER */
/*
alter table `closed_deals` (
    ADD CONSTRAINT fk_closed_deals_salespersons FOREIGN KEY (`salesperson_id`) REFERENCES `salespersons`(`id`)
);
*/
