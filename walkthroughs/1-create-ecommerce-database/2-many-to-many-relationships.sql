use `ecommerce`;

create table `purchases` (
    `purchase_id` INT AUTO_INCREMENT PRIMARY KEY,
    `customer_id` INT NOT NULL,
    `product_id` INT NOT NULL,
    `date_purchased` DATETIME NOT NULL,
    FOREIGN KEY (`customer_id`) REFERENCES `customers`(`customer_id`),
    FOREIGN KEY (`product_id`) REFERENCES `products`(`product_id`)
);