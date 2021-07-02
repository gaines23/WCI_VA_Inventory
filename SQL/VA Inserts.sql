
USE Inventory_VA

INSERT INTO Department(Department)
VALUES('Oncology')
INSERT INTO Department(Department)
VALUES('Emergency Room')
INSERT INTO Department(Department)
VALUES('Cafeteria')
INSERT INTO Department(Department)
VALUES('Custodial')
INSERT INTO Department(Department)
VALUES('Nursing')
INSERT INTO Department(Department)
VALUES('Radiology')



INSERT INTO Job(Job)
VALUES('Doctor')
INSERT INTO Job(Job)
VALUES('Nurse')
INSERT INTO Job(Job)
VALUES('Janitor')
INSERT INTO Job(Job)
VALUES('Housekeeping')
INSERT INTO Job(Job)
VALUES('Intern')
INSERT INTO Job(Job)
VALUES('Specialist')
INSERT INTO Job(Job)
VALUES('On Call')
INSERT INTO Job(Job)
VALUES('Receptionist')






INSERT INTO Employee(EmpFirstName, EmpLastName, DateAdded, Job, Department)
VALUES('Melissa', 'Gaines', '4/1/2021', 'Doctor', 'Oncology')

INSERT INTO Employee(EmpFirstName, EmpLastName, DateAdded, Job, Department)
VALUES('Jeff', 'Benson', '3/21/2021', 'Nurse', 'Emergency Room')

INSERT INTO Employee(EmpFirstName, EmpLastName, DateAdded, Job, Department)
VALUES('Michael', 'Diplan', '1/15/2021', 'Specialist', 'Radiology')

INSERT INTO Employee(EmpFirstName, EmpLastName, DateAdded, Job, Department)
VALUES('Jason', 'Dale', '2/7/2021', 'On Call', 'Radiology')

INSERT INTO Employee(EmpFirstName, EmpLastName, DateAdded, Job, Department)
VALUES('Melissa', 'Gaines', '4/1/2021', 'Receptionist', 'Nursing')








INSERT INTO AssignEmpGarm(EmployeeID, DateAssigned, Quantity, Replacement, GarmType, GarmSize)
VALUES(1, '5/16/2021', 2, 'No', 'Shirt', 'Medium')
INSERT INTO AssignEmpGarm(EmployeeID, DateAssigned, Quantity, Replacement, GarmType, GarmSize)
VALUES(1, '4/16/2021', 3, 'No', 'Pants', 'Medium')
INSERT INTO AssignEmpGarm(EmployeeID, DateAssigned, Quantity, Replacement, GarmType, GarmSize)
VALUES(1, '5/1/2021', 2, 'Yes', 'Scrubs', 'Small')

INSERT INTO AssignEmpGarm(EmployeeID, DateAssigned, Quantity, Replacement, GarmType, GarmSize)
VALUES(2, '4/16/2021', 2, 'Yes', 'Shirt', 'Large')
INSERT INTO AssignEmpGarm(EmployeeID, DateAssigned, Quantity, Replacement, GarmType, GarmSize)
VALUES(2, '4/16/2021', 3, 'No', 'Scrub Pants', 'Large')
INSERT INTO AssignEmpGarm(EmployeeID, DateAssigned, Quantity, Replacement, GarmType, GarmSize)
VALUES(2, '4/16/2021', 2, 'Yes', 'Black Shoes', '10')


INSERT INTO AssignEmpGarm(EmployeeID, DateAssigned, Quantity, Replacement, GarmType, GarmSize)
VALUES(3, '4/16/2021', 2, 'Yes', 'Shirt', 'Large')
INSERT INTO AssignEmpGarm(EmployeeID, DateAssigned, Quantity, Replacement, GarmType, GarmSize)
VALUES(3, '4/16/2021', 3, 'No', 'Srub Pants', 'Large')
INSERT INTO AssignEmpGarm(EmployeeID, DateAssigned, Quantity, Replacement, GarmType, GarmSize)
VALUES(3, '4/16/2021', 2, 'No', 'Black Shoes', '10')


SELECT * FROM Department 
SELECT * FROM Job

SELECT * FROM Employee


SELECT * FROM AssignEmpGarm where EmployeeID = 6

where EmployeeID = 1

SELECT * FROM SearchEmpInfo

DELETE FROM Employee

DELETE FROM AssignEmpGarm
