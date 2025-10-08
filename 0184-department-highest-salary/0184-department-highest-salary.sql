# Write your MySQL query statement below
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d
ON e.departmentId = d.id
WHERE 
    (e.salary, e.departmentId) IN (
        SELECT 
            MAX(salary) AS max_salary,
            departmentId
        FROM Employee
        GROUP BY departmentId
    );