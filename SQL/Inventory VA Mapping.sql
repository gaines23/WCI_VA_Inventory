
USE master
GO

IF DB_ID('Inventory_VA') IS NOT NULL
	DROP DATABASE Inventory_VA;

CREATE DATABASE Inventory_VA;
GO

USE Inventory_VA;
GO

CREATE TABLE Employee(
	EmployeeID INT IDENTITY(1,1) NOT NULL PRIMARY KEY
	, EmpFirstName VARCHAR(20)
	, EmpLastName VARCHAR(20)
	, DateAdded DATE
	, EmpFullName VARCHAR(MAX)
	, Department VARCHAR(MAX)
	, Job VARCHAR(MAX)
)


-- If I can get Django Update to work, use this table
-- This is where the assignment for Emp and Garm go
CREATE TABLE AssignEmpGarm(
	GarmentID INT IDENTITY(1,1) NOT NULL PRIMARY KEY
	, EmployeeID INT
	, DateAssigned DATE
	, Quantity INT 
	, Replacement VARCHAR(10)
	, GarmType VARCHAR(MAX) -- Shirt, pants, shoes etc
	, GarmSize VARCHAR(MAX)
	, FOREIGN KEY(EmployeeID) REFERENCES Employee(EmployeeID)
)
