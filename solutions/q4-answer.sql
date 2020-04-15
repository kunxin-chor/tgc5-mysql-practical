create database `tv_shows`;

create table `tv_series`(
    `show_id` INT AUTO_INCREMENT PRIMARY KEY,
    `series_name` VARCHAR(45) NOT NULL,
    `plot_summary` TEXT NOT NULL
);

create table `episodes`(
    `episode_id` INT AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(45) NOT NULL,
    `duration` INT NOT NULL,
    `synopsis` TEXT NOT NULL,
    `show_id` INT NOT NULL,
     CONSTRAINT show_id_episodes_id FOREIGN KEY (`show_id`) REFERENCES `tv_series`(`show_id`)
);


