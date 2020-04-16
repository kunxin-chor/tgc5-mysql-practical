# SELECT Statements for ClassicModels

## Preliminary steps to explore a database:

1. `use <database name>;`

2. `show tables;`

3. `describe <table name>;`

## The BASICS

At its core, the SELECT statement let's us select columns from all rows in a table.

`select <columns> FROM <table name>`

### SELECT *
The `*` refers to ALL COLUMNS

### select all columns in all rows from the offices table
    select * from `offices`;

### select certain columns
    select `city`,`country` FROM `offices`;

### select certain rows (filtering)
    select <columns> FROM <table> WHERE <condition1> AND/OR <condition2>
Example:
    /* show offices in the USA */
    select * from offices where country='USA';

    /* show phone numbers and city of offices in the USA*/
    select city,phone from offices where country="USA";

### GROUP BY

#### Find the count of each product line
    SELECT `productLine`,count(*) FROM `products` GROUP BY `productLine`;

### Find the max price of each product line
    SELECT `productLine`,count(*) FROM `products` GROUP BY `productLine`;

#### Find average credit limit for each country
    SELECT `country`, AVG(`creditLimit`) FROM `customers` GROUP BY `country`;

#### Find the average credit limit of each country, excluding rows that have credit limit of 0
    SELECT `country`, AVG(`creditLimit`) FROM `customers` WHERE `creditLimit` > 0 GROUP BY `country`;

### Find the number of custoemrs per country,but only show those countries with more than 5 customers
    SELECT `country`, count(*) FROM `customers` GROUP BY `country` HAVING count(*) > 5


# ORDER OF Statements
    select <colnames>
     from <table>
        join <table> on <cond>
    where <cond>
    group by <col>
        having <cond>
    order by <col> ASC|DESC
    limit <number of rows>

1. FROM and JOIN will happen first
2. WHERE will happen
3. GROUP BY
4. SELECT
5. HAVING
6. ORDER BY
7. LIMIT

## JOINS

### Display the office address of each employee
    SELECT `firstName`, `lastName`, `city`, `addressLine1`, `addressLine2`
     FROM `employees` JOIN `offices` ON `employees`.`officeCode` = `offices`.`officeCode`

### Display the office address of each employee based in Paris
    SELECT `firstName`, `lastName`, `city`, `addressLine1`, `addressLine2`
    FROM `employees` JOIN `offices` ON `employees`.`officeCode` = `offices`.`officeCode`
    WHERE `city`='Paris';

### Display the office address of each employee based in the USA
    SELECT `firstName`, `lastName`, `city`, `addressLine1`, `addressLine2`
     FROM `employees` JOIN `offices` ON `employees`.`officeCode` = `offices`.`officeCode`
    WHERE `country`='USA'

### Display the office address of each employee NOT based in USA
    SELECT `firstName`, `lastName`, `city`, `addressLine1`, `addressLine2` FROM `employees` 
    JOIN `offices` ON `employees`.`officeCode` = `offices`.`officeCode` 
    WHERE `country`!='USA'

### Show the number of employees for each city
    SELECT `city`, COUNT(*) FROM `offices` JOIN `employees` ON `offices`.`officeCode` = `employees`.`officeCode` GROUP BY `city`

### Find all employees which job title begins with "Sales"
    SELECT * FROM `employees` WHERE `jobTitle` LIKE 'Sales%';

### Find all employees which job title ends with "Sales"
    SELECT * FROM `employees` WHERE `jobTitle` LIKE '%Sales'    

### Find all employees which job title contains "Sales"
    SELECT * FROM `employees` WHERE `jobTitle` LIKE '%Sales%'

## DATE/TIME STUFF

### Insert a new payment
    insert into `payments` (`customerNumber`, `checkNumber`, `paymentDate`, `amount`)
    VALUES
        ('496', 'ABC12212', NOW(), '2500');

### Find payment made within certaind days
    select customerNumber, checkNumber, paymentDate, DATEDIFF(NOW(), `paymentDate`)  from `payments` where DATEDIFF(NOW(),`paymentDate`) <=3;

### Display all payments sorted by date
    select * from payments order by `paymentDate`;

### DIsplay the top 10 payments made by amount
    select * from payments order by `amount` DESC limit 10;

# CHALLENGES

## For each product group, find the product with the max buy price

