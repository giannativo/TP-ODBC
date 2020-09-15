USE sakila;
DELIMITER //

DROP PROCEDURE IF EXISTS SetAddressAndCustomer //

CREATE PROCEDURE SetAddressAndCustomer(
	IN first_name VARCHAR(45), IN last_name VARCHAR(45), IN store_id INT(3), IN email VARCHAR(50), IN address VARCHAR(50),
    IN district VARCHAR(20), IN city_id INT(5), IN postal_code INT(10), IN phone VARCHAR(20))
BEGIN
	INSERT INTO address(address, district, city_id, postal_code, phone, location) VALUES (address, district, city_id, postal_code,
    phone, ST_GeomFromText('POINT (30 10)'));
    SET @address_id = LAST_INSERT_ID();
    INSERT INTO customer(store_id, first_name, last_name, email, address_id, active) VALUES (store_id, first_name, last_name, email,
    @address_id, TRUE);
END //

DROP PROCEDURE IF EXISTS GetCustomer //

CREATE PROCEDURE GetCustomer(IN first_name VARCHAR(45), IN last_name VARCHAR(45), IN city_id INT(5))
BEGIN
	SELECT cust.customer_id, cust.store_id, cust.first_name, cust.last_name, cust.email, 
    cust.active, a.address, a.district, a.postal_code, a.phone, city.city, country.country, city.city_id, a.address_id 
    FROM customer cust 
    INNER JOIN address a 
    ON cust.address_id = a.address_id
    INNER JOIN city
    ON a.city_id = city.city_id
    INNER JOIN country
    ON city.country_id = country.country_id
    WHERE (first_name IS NULL OR cust.first_name = first_name)
    AND (last_name IS NULL OR cust.last_name = last_name)
    AND (city_id IS NULL OR a.city_id = city_id);
END //

DROP PROCEDURE IF EXISTS GetCustomerById //

CREATE PROCEDURE GetCustomerById(IN customer_id INT(5))
BEGIN
	SELECT cust.customer_id, cust.store_id, cust.first_name, cust.last_name, cust.email, 
    cust.active, a.address, a.district, a.postal_code, a.phone, city.city, country.country, city.city_id, a.address_id 
    FROM customer cust 
    INNER JOIN address a 
    ON cust.address_id = a.address_id
    INNER JOIN city
    ON a.city_id = city.city_id
    INNER JOIN country
    ON city.country_id = country.country_id
    WHERE cust.customer_id = customer_id;
END //

DROP PROCEDURE IF EXISTS DeleteCustomer //

CREATE PROCEDURE DeleteCustomer(IN customer_id INT(5))
BEGIN
	UPDATE customer SET customer.active = false WHERE customer.customer_id = customer_id;
END //

DROP PROCEDURE IF EXISTS ModifyAddressAndCustomer //

CREATE PROCEDURE ModifyAddressAndCustomer(
	IN first_name VARCHAR(45), IN last_name VARCHAR(45), IN store_id INT(3), IN email VARCHAR(50), IN address VARCHAR(50),
    IN district VARCHAR(20), IN city_id INT(5), IN postal_code INT(10), IN phone VARCHAR(20), IN address_id INT(3), IN customer_id INT(3))
BEGIN
	UPDATE address
    SET address.address = address, address.district = district, address.city_id= city_id, address.postal_code = postal_code,
    address.phone = phone WHERE address.address_id = address_id;
	UPDATE customer
    SET customer.first_name = first_name, customer.last_name = last_name, customer.email = email WHERE customer.customer_id = customer_id;    
END //

DELIMITER ;
