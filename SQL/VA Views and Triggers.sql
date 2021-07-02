/* VIEWS */


-- Employee Landing Search Categories
CREATE VIEW SearchEmpInfo
AS
SELECT
	emp.EmployeeID
	, emp.EmpFirstName AS 'EmpFirstName'
	, emp.EmpLastName AS 'EmpLastName'
	, emp.Job AS 'Job'
	, emp.Department AS 'Department'
	, emp.DateAdded
FROM
	Employee AS emp


-- Creates Employee Full Name, adds name of Job and Dept
CREATE TRIGGER EmpFullName
ON Employee
AFTER INSERT, UPDATE 
AS
BEGIN
	UPDATE Employee
	SET 
		EmpFullName = CONCAT(EmpFirstName , ' ' , EmpLastName)
	FROM
		Employee
	WHERE
		EmployeeID = EmployeeID

END
