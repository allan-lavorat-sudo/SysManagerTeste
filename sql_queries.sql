-- Top 5 clientes com maior receita
SELECT customer_id, SUM(price) as total_revenue
FROM sales
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 5;

-- Top 5 produtos mais vendidos
SELECT product_id, SUM(quantity) as total_quantity
FROM sales
GROUP BY product_id
ORDER BY total_quantity DESC
LIMIT 5;
