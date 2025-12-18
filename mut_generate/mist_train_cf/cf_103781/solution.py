"""
QUESTION:
Write a SQL query named "list_recent_customer_purchases" that retrieves the names of customers, their total order amount, and the corresponding order date. The query should join the Customers, Orders, and Items tables, filter orders from the last 30 days, group results by customer name and order date, and sort the results by total order amount in descending order.
"""

def list_recent_customer_purchases(cur):
    cur.execute("""
        SELECT c.name, SUM(o.amount) AS total_order_amount, o.order_date
        FROM Customers c
        INNER JOIN Orders o ON c.customer_id = o.customer_id
        INNER JOIN Items i ON o.item_id = i.item_id
        WHERE o.order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
        GROUP BY c.name, o.order_date
        ORDER BY total_order_amount DESC
    """)
    return cur.fetchall()