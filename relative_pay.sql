SELECT e1.name AS lower_earner, e2.name AS higher_earner
FROM EMPLOYEE e1
INNER JOIN EMPLOYEE e2 ON e1.salary < e2.salary
ORDER BY e1.id ASC, e2.salary ASC;
