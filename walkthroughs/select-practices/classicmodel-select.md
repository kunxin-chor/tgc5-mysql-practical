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