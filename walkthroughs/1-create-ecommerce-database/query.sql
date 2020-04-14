create database `ecommerce`;

use `ecommerce`;

create table `customers` (
    `customer_id` INT AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(100) NOT NULL,
    `last_name` VARCHAR(100) NOT NULL
);

insert into `customers` (`first_name`, `last_name`) 
values ('Ah Kow', 'Tan');

insert into `customers` (`first_name`,`last_name`)
values ('Cindy', 'Gao');

select * from `customers`;

alter table `customers`
    ADD `date_joined` DATETIME;

/* change the column name */
alter table `customers`
    change `date_joined` `joined_date` datetime;

/* updating existing rows */
update `customers` set `date_joined` = NOW() where `customer_id` = 1; 
