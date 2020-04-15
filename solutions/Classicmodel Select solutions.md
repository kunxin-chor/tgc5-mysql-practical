## Get first name, last name ande email of employees
    select firstname, lastname, email from employees;

## get email, first name and last name of all emplyoees who are sales rep
    select firstname, lastname, email from employees where jobTitle =  'Sales Rep' order by firstname desc;

## get all employees from office code 1
    select * from employees where jobTitle='Sales Rep' AND officeCode = '1'