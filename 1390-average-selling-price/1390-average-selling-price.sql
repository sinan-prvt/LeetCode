# Write your MySQL query statement below
SELECT p.product_id , ROUND(
    IFNULL(SUM(u.units * pr.price) / SUM(u.units), 0), 2
) AS average_price
FROM (SELECT DISTINCT product_id FROM Prices) p
LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id
LEFT JOIN Prices pr
    ON u.product_id = pr.product_id
    AND u.purchase_date BETWEEN pr.start_date AND pr.end_date
GROUP BY p.product_id