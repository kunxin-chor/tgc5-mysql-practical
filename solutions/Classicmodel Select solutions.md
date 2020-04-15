## Get first name, last name ande email of employees
    select firstname, lastname, email from employees;

## get email, first name and last name of all emplyoees who are sales rep
    select firstname, lastname, email from employees where jobTitle =  'Sales Rep' order by firstname desc;

## get all employees from office code 1
    select * from employees where jobTitle='Sales Rep' AND officeCode = '1'

## count how many employees there are for each office code
    select`officeCode`, count(*) from `employees` group by `officeCode`

## show the average spent of each customer form the payment
    select `customerNumber`, avg(`amount`) from `payments` group by `customerNumber`

## show the average spent of each customer form the payment but only if that custoemr has spent at least average of 10k
     select `customerNumber`, avg(`amount`) from `payments` group by `customerNumber` having avg(`amount`) >= '10000';

## show the average spent for each customer but only consider each time when the customer spent more than 10k
    select `customerNumber`, avg(`amount`) from `payments` where `amount` >= '10000'  group by `customerNumber`; 

## show the number of payments made by customer, with the most orders first
    select `customerNumber`, count(*) from `payments` group by `customerNumber` ORDER BY `count(*)` DESC;


## Show the first name, last name, email and city of each employee
    select `firstName`, `lastName`, `email`, `city` FROM `employees` 
        JOIN `offices` ON `offices`.`officeCode` = `employees`.`officeCode`;

## Show all customers and their average amount spent if they have spent an average amount of 10K or higher
    select `customerName`, avg(`amount`) FROM `customers` JOIN `payments` ON `payments`.`customerNumber` = `customers`.`customerNumber`
        group by `customerName` HAVING avg(`amount`) >= 10000;

## Show all custoemrs and their average amount spent if they have spent an aerage amount of 10k or higher and is from the USA:
    select `customerName`, avg(`amount`) 
    FROM `customers` 
        JOIN `payments` ON `payments`.`customerNumber` = `customers`.`customerNumber` 
    where `customers`.`country` ='USA'
    group by `customerName` 
        HAVING avg(`amount`) >= 10000