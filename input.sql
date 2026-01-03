-- Create table If Not Exists Employee (id int, name varchar(255), salary int, managerId int);
-- Truncate table Employee;
-- insert into Employee (id, name, salary, managerId) values ('1', 'Joe', '70000', '3');
-- insert into Employee (id, name, salary, managerId) values ('2', 'Henry', '80000', '4');
-- insert into Employee (id, name, salary, managerId) values ('3', 'Sam', '60000', NULL);
-- insert into Employee (id, name, salary, managerId) values ('4', 'Max', '90000', NULL);

Create table If Not Exists Person (personId int, firstName varchar(255), lastName varchar(255));
Create table If Not Exists Address (addressId int, personId int, city varchar(255), state varchar(255));
Truncate table Person;
insert into Person (personId, lastName, firstName) values ('1', 'Wang', 'Allen');
insert into Person (personId, lastName, firstName) values ('2', 'Alice', 'Bob');
Truncate table Address;
insert into Address (addressId, personId, city, state) values ('1', '2', 'New York City', 'New York');
insert into Address (addressId, personId, city, state) values ('2', '3', 'Leetcode', 'California');