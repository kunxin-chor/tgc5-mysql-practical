create database `movies`;

use  `movies`;

create table `movies` (
    `movie_id` int AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(100) NOT NULL 
);

create table `actors` (
    `actor_id` INT AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(100) NOT NULL,
    `last_name` VARCHAR(100) NOT NULL,
    `gender` TINYINT NOT NULL
);

create table `castings` (
    `casting_id` INT AUTO_INCREMENT PRIMARY KEY,
    `actor_id` INT NOT NULL,
    `movie_id` INT NOT NULL,
    FOREIGN KEY (`actor_id`) REFERENCES `actors`(`actor_id`),
    FOREIGN KEY (`movie_id`) REFERENCES `movies`(`movie_id`)
);

insert into actors (`first_name`, `last_name`, `gender`)
VALUES
    ('Liv', 'Tyler', '1'),
    ('Viggo', 'Mortensen', '0'),
    ('Robert', 'Downey Junior', '0'),
    ('Jeff', 'Bridges', '0');

insert into movies (`title`)
VALUES
    ('Lord of the Rings'), ('Ironman'), ('Avengers'),('Avengers: Endgame'),('Avengers: Infinity War');



insert into `castings` (`actor_id`, `movie_id`)
VALUES
    ('1', '1'),
    ('2', '1'),
    ('3', '2'),
    ('3', '3'),
    ('3', '4'),
    ('3', '5'),
    ('4', '2');

SELECT * FROM `actors` 
    JOIN `castings` ON `actors`.`actor_id` = `castings`.`actor_id`;
    
SELECT * FROM `actors` 
    JOIN `castings` ON `actors`.`actor_id` = `castings`.`actor_id`
    JOIN `movies` ON `movies`.`movie_id` = `castings`.`movie_id`;
    
/*
    (actors x castings) x movies
*/